from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add(
        "",
        [("完成率", 66.6)],
        title_label_opts=opts.LabelOpts(
            font_size=40, color="blue", font_family="Microsoft YaHei"
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-改变轮盘内的字体"))
    
)

c.width = "100%"
put_html(c.render_notebook())
