import argparse
import re
from os import path

from bokeh_demo import bokehs
from cutecharts_demo import cutecharts
from plotly_demo import plotly_demo
from pyecharts_demo import pyecharts
from pywebio import start_server
from pywebio.output import put_markdown
from pywebio.session import set_env


async def index():
    set_env(title="PyWebIO Chart Gallery")
    readme_file = path.join(path.dirname(__file__), "README.md")
    readme = open(readme_file).read()

    readme = re.sub(r"\[\*\*demos\*\*\]\(.*?\?pywebio_api=(.+?)\)", r"[**demos**](./?pywebio_api=\g<1>)", readme)
    cdn = r"https://cdn.jsdelivr.net/gh/wang0618/pywebio-chart-gallery@master"
    github_url = r"https://raw.githubusercontent.com/wang0618/pywebio-chart-gallery/master"
    readme = readme.replace(github_url, cdn)
    readme = re.sub(r"<div></div>[\s\S]*$", "", readme)

    put_markdown(readme)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PyWebIO Chart Gallery")
    parser.add_argument('port', default=8080, help="run on the given port", type=int)
    parser.add_argument('--debug', action="store_true")
    args = parser.parse_args()

    start_server({
        'index': index,
        'cutecharts': cutecharts,
        'pyecharts': pyecharts,
        'plotly': plotly_demo,
        'bokeh': bokehs,
    }, port=args.port, debug=args.debug)
