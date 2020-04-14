from collections import OrderedDict

from pywebio.input import actions
from pywebio.output import *
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


def show_demo(name):
    if name not in all_demos:
        return

    clear_after('demo-start')
    all_demos[name]()

    put_html('<a href="https://github.com/wang0618/pywebio-chart-gallery/blob/master'
             '/cutecharts_demo/demos/example_%s.py" target="_blank">源码</a>' % name.lower())


def cutecharts():
    set_auto_scroll_bottom(False)

    put_markdown(r"""## Cutecharts.py
    
    [cutecharts.py](https://github.com/cutecharts/cutecharts.py) 是一个创建具有卡通风格的可视化图表的python库。底层使用了 [chart.xkcd](https://github.com/timqian/chart.xkcd) Javascript库。
    
    PyWebIO 支持输出使用 cutecharts.py 库创建的图表。使用方式为在PyWebIO会话中调用 
    ```python
    # chart 为 cutecharts 的图表实例
    pywebio.output.put_html(chart.render_notebook())
    ``` 
    具体可以参考下面demo中的源码。

    ## Demos List
    """, strip_indent=4)

    put_buttons(list(all_demos.keys()), onclick=show_demo)
    set_anchor('demo-start')

    actions(buttons=['退出'])
