from collections import OrderedDict

from pywebio.output import *
from pywebio.session import info as session_info
from .demos.example_bar import main as bar
from .demos.example_line import main as line
from .demos.example_page import main as page
from .demos.example_pie import main as pie
from .demos.example_radar import main as radar
from .demos.example_scatter import main as scatter

all_demos = OrderedDict([
    ("Bar", bar),
    ("Line", line),
    ("Pie", pie),
    ("Radar", radar),
    ("Scatter", scatter),
    ("Page", page),
])


def t(eng, chinese):
    """return English or Chinese text according to the user's browser language"""
    return chinese if 'zh' in session_info.user_language else eng


@use_scope('demo', clear=True)
def show_demo(name):
    if name not in all_demos:
        return

    all_demos[name]()

    put_html('<a href="https://github.com/wang0618/pywebio-chart-gallery/blob/master'
             '/cutecharts_demo/demos/example_%s.py" target="_blank">%s</a>' % (name.lower(), t('Source code', '源码')))

    scroll_to('demo-list', 'top')


async def cutecharts():
    """PyWebIO cutechart Demo

    Demo of using cutechart.py for data visualization in PyWebIO.
    在PyWebIO中使用 cutechart.py 进行数据可视化示例"""

    put_markdown(t(r"""## Cutecharts.py
    
    [cutecharts.py](https://github.com/cutecharts/cutecharts.py) is a hand drawing style charts library for Python which uses [chart.xkcd](https://github.com/timqian/chart.xkcd) as underlying implementation.

    With [PyWebIO](https://github.com/wang0618/PyWebIO), you can use the following code to output the cutecharts.py chart instance:

    ```python
    # `chart` is cutecharts chart instance
    pywebio.output.put_html(chart.render_notebook())
    ``` 
    For details, please refer to the source code of the demo below.

    ## Demos List
    """, r"""## Cutecharts.py
    
    [cutecharts.py](https://github.com/cutecharts/cutecharts.py) 是一个可以创建具有卡通风格的可视化图表的python库。底层使用了 [chart.xkcd](https://github.com/timqian/chart.xkcd) Javascript库。
    
    [PyWebIO](https://github.com/wang0618/PyWebIO) 支持输出使用 cutecharts.py 库创建的图表。使用方式为在PyWebIO会话中调用 
    ```python
    # chart 为 cutecharts 的图表实例
    pywebio.output.put_html(chart.render_notebook())
    ``` 
    具体可以参考下面demo中的源码。

    ## Demos List
    """), strip_indent=4)
    set_scope('demo-list')

    put_buttons(list(all_demos.keys()), onclick=show_demo)
