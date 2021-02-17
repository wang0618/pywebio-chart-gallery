import os
import json
from collections import OrderedDict
from functools import partial
from os import path

import pywebio
from pywebio.output import *
from pywebio.session import hold, get_info

src_path = path.join(path.dirname(__file__), "demos")

all_demos_zh = OrderedDict(json.load(open(path.join(path.dirname(__file__), 'inventory.json'))))
all_demos = OrderedDict({i: i for i in all_demos_zh.keys()})


def t(eng, chinese):
    """return English or Chinese according to the user's browser language"""
    return chinese if 'zh' in get_info().user_language else eng


@use_scope('content', clear=True)
def show_demo(name):
    if name not in t(all_demos, all_demos_zh):
        return

    with use_scope('loading'):
        put_text('Loading...')
        put_loading()

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

        # todo: if there is `open` calls, provide the file link
        put_collapse(t('Show source code', '查看源码'), put_code(code, 'python'))

    scroll_to(position='top')
    clear('loading')


async def pyecharts():
    """PyWebIO pyecharts Demo

    Demo of using pyecharts for data visualization in PyWebIO.
    在PyWebIO中使用 pyecharts 进行数据可视化示例
    """

    put_markdown(t(r"""## pyecharts

    [pyecharts](https://github.com/pyecharts/pyecharts) is a python plotting library which uses [Echarts](https://github.com/ecomfe/echarts) as underlying implementation.

    In PyWebIO, you can use the following code to output the pyecharts chart instance:

    ```python
    # chart is pyecharts chart instance
    pywebio.output.put_html(chart.render_notebook())
    ``` 
    For details, please refer to the source code of the demo below.

    ## Demos List
    """, r"""## pyecharts

    [pyecharts](https://github.com/pyecharts/pyecharts) 是一个使用Python创建 [Echarts](https://github.com/ecomfe/echarts) 可视化图表的库。

    PyWebIO 支持输出使用 pyecharts 库创建的图表。使用方式为在PyWebIO会话中调用：
    ```python
    # chart 为 pyecharts 的图表实例
    pywebio.output.put_html(chart.render_notebook())
    ``` 
    具体可以参考下面demo中的源码。

    ## Demos List
    """), strip_indent=4)

    put_buttons([(v, k) for k, v in t(all_demos, all_demos_zh).items()], onclick=show_demo)
    put_markdown('----')
    set_scope('content')
    set_scope('loading')

    await hold()
