from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType

c = (
    Liquid()
    .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.RECT)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-rect"))
    
)

c.width = "100%"
put_html(c.render_notebook())
