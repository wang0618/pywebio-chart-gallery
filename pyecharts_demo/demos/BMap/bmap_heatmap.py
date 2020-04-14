from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.faker import Faker

c = (
    BMap()
    .add_schema(baidu_ak="FAKE_AK", center=[120.13066322374, 30.240018034923])
    .add(
        "bmap",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        type_="heatmap",
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="BMap-热力图"), visualmap_opts=opts.VisualMapOpts()
    )
    
)

c.width = "100%"
put_html(c.render_notebook())