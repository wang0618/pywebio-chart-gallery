from collections import OrderedDict

from pywebio.output import *
from pywebio.session import info as session_info
import os

here_dir = os.path.dirname(os.path.abspath(__file__))

all_demos = OrderedDict([
    (f.upper()[0] + f[1:-3], open('%s/demos/%s' % (here_dir, f)).read())
    for f in os.listdir(here_dir + '/demos')
])


def t(eng, chinese):
    """return English or Chinese text according to the user's browser language"""
    return chinese if 'zh' in session_info.user_language else eng


@use_scope('demo', clear=True)
def show_demo(name):
    if name not in all_demos:
        return

    exec(all_demos[name])

    put_html('<a href="https://github.com/wang0618/pywebio-chart-gallery/blob/master'
             '/pyg2plot_demo/demos/%s.py" target="_blank">%s</a>' % (name.lower(), t('Source code', '源码')))

    scroll_to('demo-list', 'top')


async def pyg2plot():
    """PyWebIO pyg2plot Demo

    Demo of using pyg2plot for data visualization in PyWebIO.
    在PyWebIO中使用 pyg2plot进行数据可视化示例"""

    put_markdown(t(r"""## pyg2plot
    
    [pyg2plot](https://github.com/hustcc/PyG2Plot) is a python plotting library which uses [G2Plot](https://github.com/antvis/G2Plot) as underlying implementation.

    With [PyWebIO](https://github.com/wang0618/PyWebIO), you can use the following code to output the pyg2plot chart instance:

    ```python
    # `chart` is pyg2plot chart instance
    pywebio.output.put_html(chart.render_notebook())
    ``` 
    For details, please refer to the source code of the demo below.

    ## Demos List
    """, r"""## pyg2plot
    
    [pyg2plot](https://github.com/hustcc/PyG2Plot) 是一个使用Python创建 [G2Plot](https://github.com/antvis/G2Plot) 可视化图表的库。
    
    [PyWebIO](https://github.com/wang0618/PyWebIO) 支持输出使用 pyg2plot 库创建的图表。使用方式为在PyWebIO会话中调用 
    ```python
    # chart 为 pyg2plot 的图表实例
    pywebio.output.put_html(chart.render_notebook())
    ``` 
    具体可以参考下面demo中的源码。

    ## Demos List
    """), strip_indent=4)
    set_scope('demo-list')

    put_buttons(list(all_demos.keys()), onclick=show_demo)
