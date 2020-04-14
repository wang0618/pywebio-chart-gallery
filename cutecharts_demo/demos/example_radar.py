from cutecharts.charts import Radar
from cutecharts.components import Page
from cutecharts.faker import Faker

from pywebio import start_server
from pywebio.output import put_html


def radar_base() -> Radar:
    chart = Radar("Radar-基本示例")
    chart.set_options(labels=Faker.choose())
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart


def radar_legend_colors():
    chart = Radar("Radar-颜色调整")
    chart.set_options(labels=Faker.choose(), colors=Faker.colors, legend_pos="upRight")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart


def main():
    page = Page()
    page.add(radar_base(), radar_legend_colors())
    put_html(page.render_notebook())


if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
