from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

try:
    register_url("https://echarts-maps.github.io/echarts-china-counties-js/")
except Exception:
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context
    register_url("https://echarts-maps.github.io/echarts-china-counties-js/")

c = (
    Geo()
    .add_schema(maptype="海淀区")
    .set_global_opts(title_opts=opts.TitleOpts(title="海淀区"))
    
)

c.width = "100%"
put_html(c.render_notebook())
