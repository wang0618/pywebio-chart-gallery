from cutecharts.charts import Scatter
from cutecharts.components import Page
from cutecharts.faker import Faker

from pywebio import start_server
from pywebio.output import put_html


def scatter_base() -> Scatter:
    chart = Scatter("Scatter-基本示例")
    chart.set_options(x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart


def scatter_dotsize_tickcount():
    chart = Scatter("Scatter-散点大小")
    chart.set_options(dot_size=2, y_tick_count=8)
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart


def scatter_show_line():
    chart = Scatter("Scatter-散点连成线")
    chart.set_options(y_tick_count=8, is_show_line=True)
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart


def main():
    page = Page()
    page.add(scatter_base(), scatter_dotsize_tickcount(), scatter_show_line())
    put_html(page.render_notebook())


if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
