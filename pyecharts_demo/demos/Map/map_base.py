from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

c = (
    Map()
    .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    
)

c.width = "100%"
put_html(c.render_notebook())
