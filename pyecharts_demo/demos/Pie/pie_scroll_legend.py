from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add(
        "",
        [
            list(z)
            for z in zip(
                Faker.choose() + Faker.choose() + Faker.choose(),
                Faker.values() + Faker.values() + Faker.values(),
            )
        ],
        center=["40%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-Legend 滚动"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    
)

c.width = "100%"
put_html(c.render_notebook())
