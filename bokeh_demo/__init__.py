import json
import re
from functools import partial
from os import path

from bokeh.io import output_notebook

from pywebio import config
from pywebio.output import *
from pywebio.session import info as session_info

here_dir = path.dirname(path.abspath(__file__))
demos_dir = path.join(here_dir, 'demos')

demos = json.load(open(path.join(here_dir, 'inventory.json')))

demo_set = set(demos)

style = """
.bokeh-demo-link:hover {
    transition-duration: 400ms;
    transform: translateY(-2px);
    -webkit-box-shadow: 0 50px 80px -20px rgba(0, 0, 0, .27), 0 30px 50px -30px rgba(0, 0, 0, .3);
    box-shadow: 0 50px 80px -20px rgba(0, 0, 0, .27), 0 30px 50px -30px rgba(0, 0, 0, .3);
}
"""


def t(eng, chinese):
    """return English or Chinese text according to the user's browser language"""
    return chinese if 'zh' in session_info.user_language else eng


@use_scope('demo', clear=True)
def show_demo(name):
    if name not in demo_set:
        return

    put_markdown('-------')
    scroll_to('demo', Position.TOP)
    with use_scope('loading'):
        put_text('Loading...')
        put_loading()

    script = open(path.join(demos_dir, name + '.py')).read()

    exec_script = re.sub(r'output_file\(.*?\)', "", script)
    exec(exec_script, locals(), locals())

    script = re.sub(r'output_file\(.*?\)', "output_notebook(notebook_type='pywebio')", script)
    script = 'import pywebio\nfrom bokeh.io import output_notebook\n' + script
    put_markdown("**%s**\n```python\n%s\n```" % (t('Source code', '源码'), script))

    scroll_to('demo', Position.TOP)
    clear('loading')


def get_demos_table(demos):
    images = []
    img_tpl = '<img alt="{name}" src="https://cdn.jsdelivr.net/gh/wang0618/pywebio-chart-gallery@master/assets/bokeh/{name}.png" class="bokeh-demo-link"/>'
    for demo in demos:
        img = put_html(img_tpl.format(name=demo)).onclick(partial(show_demo, name=demo))
        images.append(img)
    col = 7
    table = [images[i * col:i * col + col] for i in range((len(images) + col - 1) // col)]
    return table


@config(css_style=style)
async def bokehs():
    """PyWebIO Bokeh Demo

    Demo of using bokeh for data visualization in PyWebIO.
    在PyWebIO中使用 Bokeh 进行数据可视化的示例
    """
    put_markdown(t(r"""## Bokeh
    [PyWebIO](https://github.com/wang0618/PyWebIO) supports for data visualization with `Bokeh` library.
    
    You can use `bokeh.io.output_notebook(notebook_type='pywebio')` in the PyWebIO session to setup Bokeh environment. 
    Then you can use `bokeh.io.show()` to output a boken chart:
    %s    
    For details, please refer to the source code of the demo below.

    ## Demos List
    Click the thumbnail to view demo.
    """, r"""## Bokeh
    [PyWebIO](https://github.com/wang0618/PyWebIO) 支持使用 Bokeh 进行数据可视化。只需要在PyWebIO会话开始后调用 `bokeh.io.output_notebook()` 设置PyWebIO环境，之后对 `bokeh.io.show()` 的调用就可以将图表显示在PyWebIO页面上了。
    %s    
    具体可以参考下面demo中的源码。

    ## Demos List
    点击图片来查看相应示例
    """) % """
    ```python
    from bokeh.io import output_notebook
    from bokeh.io import show

    output_notebook(notebook_type='pywebio')
    fig = ...  # create bokeh chart
    
    show(fig)
    ``` 
    """, strip_indent=4)

    output_notebook(verbose=False, notebook_type='pywebio')

    put_table(get_demos_table(demos))
