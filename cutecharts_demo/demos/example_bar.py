from cutecharts.charts import Bar
from cutecharts.components import Page
from cutecharts.faker import Faker

from pywebio import start_server
from pywebio.output import put_html


def bar_base() -> Bar:
    chart = Bar("Bar-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    return chart


def bar_tickcount_colors():
    chart = Bar("Bar-调整颜色")
    chart.set_options(labels=Faker.choose(), y_tick_count=10, colors=Faker.colors)
    chart.add_series("series-A", Faker.values())
    return chart


def main():
    page = Page()
    page.add(bar_base(), bar_tickcount_colors())
    put_html(page.render_notebook())


if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
