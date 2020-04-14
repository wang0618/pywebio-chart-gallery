from cutecharts.components import Page

from pywebio import start_server
from pywebio.output import put_html
from .example_bar import bar_base
from .example_line import line_base
from .example_pie import pie_base
from .example_radar import radar_base
from .example_scatter import scatter_base


def main():
    page = Page()
    page.add(bar_base(), line_base(), pie_base(), radar_base(), scatter_base())
    put_html(page.render_notebook())


if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
