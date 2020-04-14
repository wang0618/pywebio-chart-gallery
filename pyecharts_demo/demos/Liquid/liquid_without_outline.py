from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Liquid

c = (
    Liquid()
    .add("lq", [0.6, 0.7, 0.8], is_outline_show=False)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-无边框"))
    
)

c.width = "100%"
put_html(c.render_notebook())
