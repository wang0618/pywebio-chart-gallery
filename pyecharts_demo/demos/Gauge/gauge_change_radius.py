from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add("", [("完成率", 66.6)], radius="50%")
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-修改 Radius 为 50%"))
    
)

c.width = "100%"
put_html(c.render_notebook())
