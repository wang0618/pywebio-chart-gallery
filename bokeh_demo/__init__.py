import os
import sys
from os import path
import logging
import re
import json
from shutil import copyfile
from collections import OrderedDict
from pywebio.io_ctrl import output_register_callback
from pywebio.session import hold
from pywebio.output import *
from bokeh.io import output_notebook
from functools import partial

here_dir = path.dirname(path.abspath(__file__))
demos_dir = path.join(here_dir, 'demos')

demos = json.load(open(path.join(here_dir, 'inventory.json')))

demo_set = set(demos)

style = """
<style>
.bokeh-demo-link:hover {
    transition-duration: 400ms;
    transform: translateY(-2px);
    -webkit-box-shadow: 0 50px 80px -20px rgba(0, 0, 0, .27), 0 30px 50px -30px rgba(0, 0, 0, .3);
    box-shadow: 0 50px 80px -20px rgba(0, 0, 0, .27), 0 30px 50px -30px rgba(0, 0, 0, .3);
}
</style>
"""


@use_scope('demo', clear=True)
def show_demo(_, name):
    if name not in demo_set:
        return

    put_markdown('-------')
    script = open(path.join(demos_dir, name + '.py')).read()

    exec_script = re.sub(r'output_file\(.*?\)', "", script)
    exec(exec_script, locals(), locals())

    script = re.sub(r'output_file\(.*?\)', "output_notebook(notebook_type='pywebio')", script)
    script = 'import pywebio\nfrom bokeh.io import output_notebook\n' + script
    put_markdown("**源码**\n```python\n%s\n```" % script)
    scroll_to('demo', Position.TOP)


def get_demos_table(demos):
    td = """
    <td>
      <a onclick="javascript:WebIO.DisplayAreaButtonOnClick(this, '{callback_id}')" value="{name}">
        <img alt="{name}" src="https://cdn.jsdelivr.net/gh/wang0618/pywebio-chart-gallery@master/assets/bokeh/{name}.png" class="bokeh-demo-link"/>
      </a>
    </td>
    """
    tds = []
    for demo in demos:
        callback_id = output_register_callback(partial(show_demo, name=demo))
        tds.append(td.format(name=demo, callback_id=callback_id))
    col = 7
    rows = ['\n'.join(tds[i * col:i * col + col]) for i in range((len(tds) + col - 1) // col)]
    table = '\n'.join("<tr>%s</tr>" % row for row in rows)
    table = "<table>%s</table>" % table

    return table


async def bokehs():
    set_auto_scroll_bottom(False)

    put_markdown(r"""## Bokeh
    PyWebIO支持使用 Bokeh 进行数据可视化。只需要在PyWebIO会话开始后调用 `bokeh.io.output_notebook()` 设置PyWebIO环境，之后对 `bokeh.io.show()` 的调用就可以将图表显示在PyWebIO页面上了。
    
    ```python
    from bokeh.io import output_notebook
    from bokeh.io import show

    output_notebook(notebook_type='pywebio')
    fig = ...  # 创建bokeh图表
    
    show(fig)
    ``` 
    具体可以参考下面demo中的源码。

    ## Demos List
    """, strip_indent=4)

    put_html(style)

    output_notebook(verbose=False, notebook_type='pywebio')

    put_html(get_demos_table(demos))

    await hold()
