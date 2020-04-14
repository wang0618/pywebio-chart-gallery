from cutecharts.charts import Pie
from cutecharts.components import Page
from cutecharts.faker import Faker

from pywebio import start_server
from pywebio.output import put_html


def pie_base() -> Pie:
    chart = Pie("Pie-基本示例")
    chart.set_options(labels=Faker.choose())
    chart.add_series(Faker.values())
    return chart


def pie_legend_font():
    chart = Pie("Pie-Legend")
    chart.set_options(
        labels=Faker.choose(),
        legend_pos="upRight",
        font_family='"Times New Roman",Georgia,Serif;',
    )
    chart.add_series(Faker.values())
    return chart


def pie_radius():
    chart = Pie("Pie-Radius")
    chart.set_options(labels=Faker.choose(), inner_radius=0)
    chart.add_series(Faker.values())
    return chart


def main():
    page = Page()
    page.add(pie_base(), pie_legend_font(), pie_radius())
    put_html(page.render_notebook())


if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
