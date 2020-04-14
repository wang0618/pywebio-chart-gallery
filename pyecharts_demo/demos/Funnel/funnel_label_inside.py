from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker


c = (
    Funnel()
    .add(
        "商品",
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Label(inside)"))
    
)

c.width = "100%"
put_html(c.render_notebook())
