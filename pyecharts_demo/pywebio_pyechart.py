import sys
from os import path

sys.path.insert(0, "/Users/wangweimin/repos/PyWebIO")
pyecharts_src_path = path.join(path.dirname(__file__), "pyecharts-gallery")
sys.path.insert(0, pyecharts_src_path)

from pywebio.output import *
from functools import partial
import pywebio
from run_all import ChartModelDict

import os

src_path = path.join(path.dirname(__file__), "pyecharts")


def demo(name):
    def show_code(btn, code, after):
        remove('code')
        # todo 检测open调用，提供文件链接
        put_code(code, 'python', after=after, anchor='code')

    assert name in ChartModelDict

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


def basic():
    set_auto_scroll_bottom(False)

    put_buttons([(v, k) for k, v in ChartModelDict.items()], onclick=demo)

    set_anchor('content_start')

    pywebio.input.actions(buttons=['退出'])
