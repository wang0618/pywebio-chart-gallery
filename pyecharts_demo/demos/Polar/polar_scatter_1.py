from pywebio.output import put_html
import random

from pyecharts import options as opts
from pyecharts.charts import Polar

c = (
    Polar()
    .add("", [(10, random.randint(1, 100)) for i in range(300)], type_="scatter")
    .add("", [(11, random.randint(1, 100)) for i in range(300)], type_="scatter")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Scatter1"))
    
)

c.width = "100%"
put_html(c.render_notebook())
