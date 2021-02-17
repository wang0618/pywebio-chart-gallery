import argparse
import re
from os import path

from bokeh_demo import bokehs
from cutecharts_demo import cutecharts
from plotly_demo import plotly_demo
from pyecharts_demo import pyecharts
from pywebio import start_server
from pywebio.output import put_markdown
from pywebio.session import get_info

readme_file = path.join(path.dirname(__file__), "README.md")
readme_zh_file = path.join(path.dirname(__file__), "README_zh.md")
readme = open(readme_file).read()
readme_zh = open(readme_zh_file).read()


async def index():
    """PyWebIO Chart Gallery

    PyWebIO supports for data visualization with the third-party libraries. This page shows the demos of data visualization using plotly, bokeh, pyecharts and cutcharts in PyWebIO.
    PyWebIO 支持使用第三方库进行数据可视化，本页面展示了在 PyWebIO 中使用plotly、bokeh、pyecharts和cutecharts进行数据可视化的示例
    """
    global readme, readme_zh

    md = readme_zh if 'zh' in get_info().user_language else readme
    md = re.sub(r"\[\*\*demos\*\*\]\(.*?\?app=(.+?)\)", r"[**demos**](./?app=\g<1>)", md)
    cdn = r"https://cdn.jsdelivr.net/gh/wang0618/pywebio-chart-gallery@master"
    github_url = r"https://raw.githubusercontent.com/wang0618/pywebio-chart-gallery/master"
    md = md.replace(github_url, cdn)
    md = re.sub(r"<div></div>[\s\S]*$", "", md)

    put_markdown(md)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PyWebIO Chart Gallery")
    parser.add_argument('port', nargs='?', default=8080, help="run on the given port", type=int)
    parser.add_argument('--debug', action="store_true")
    args = parser.parse_args()

    start_server({
        'index': index,
        'cutecharts': cutecharts,
        'pyecharts': pyecharts,
        'plotly': plotly_demo,
        'bokeh': bokehs,
    }, port=args.port, debug=args.debug)
