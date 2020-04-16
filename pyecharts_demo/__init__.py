import os
import json
from collections import OrderedDict
from functools import partial
from os import path

import pywebio
from pywebio.output import *

src_path = path.join(path.dirname(__file__), "demos")

all_demos = OrderedDict(json.load(open(path.join(path.dirname(__file__), 'inventory.json'))))


def show_code(btn, code, after):
    remove('code')
    # todo 检测open调用，提供文件链接
    put_code(code, 'python', after=after, anchor='code')


def show_demo(name):
    if name not in all_demos:
        return

    clear_after('content_start')
    base_dir = path.join(src_path, name)
    files = os.listdir(base_dir)
    for file in files:
        if not file.endswith('.py'):
            continue
        name = file[:-len(".py")]

        html_file = path.join(base_dir, 'output', name) + '.html'
        try:
            code = open(path.join(base_dir, file)).read()
            html = open(html_file).read()
        except:
            continue

        put_html(html)
        anchor = 'show-code-%s' % name
        put_buttons(['查看源码'], partial(show_code, code=code, after=anchor), anchor=anchor)


def pyecharts():
    set_auto_scroll_bottom(False)
    put_markdown(r"""## Pyecharts

    [pyecharts](https://github.com/pyecharts/pyecharts) 是一个使用Python创建 [Echarts](https://github.com/ecomfe/echarts) 可视化图表的库。

    PyWebIO 支持输出使用 pyecharts 库创建的图表。使用方式为在PyWebIO会话中调用：
    ```python
    # chart 为 pyecharts 的图表实例
    pywebio.output.put_html(chart.render_notebook())
    ``` 
    具体可以参考下面demo中的源码。

    ## Demos List
    """, strip_indent=4)

    put_buttons([(v, k) for k, v in all_demos.items()], onclick=show_demo)

    set_anchor('content_start')

    pywebio.input.actions(buttons=['退出'])
