from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Bar, Geo, Grid
from pyecharts.faker import Faker

bar = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="20%"))
)
geo = (
    Geo()
    .add_schema(maptype="china")
    .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Grid-Geo-Bar"),
    )
)

c = (
    Grid()
    .add(bar, grid_opts=opts.GridOpts(pos_top="50%", pos_right="75%"))
    .add(geo, grid_opts=opts.GridOpts(pos_left="60%"))
    
)

c.width = "100%"
put_html(c.render_notebook())
