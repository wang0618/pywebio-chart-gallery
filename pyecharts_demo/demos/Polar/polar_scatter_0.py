from pywebio.output import put_html
import random

from pyecharts import options as opts
from pyecharts.charts import Polar

data = [(i, random.randint(1, 100)) for i in range(101)]
c = (
    Polar()
    .add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Scatter0"))
    
)

c.width = "100%"
put_html(c.render_notebook())
