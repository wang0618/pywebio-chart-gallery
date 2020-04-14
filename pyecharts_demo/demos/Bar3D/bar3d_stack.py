from pywebio.output import put_html
import random

from pyecharts import options as opts
from pyecharts.charts import Bar3D

x_data = y_data = list(range(10))


def generate_data():
    data = []
    for j in range(10):
        for k in range(10):
            value = random.randint(0, 9)
            data.append([j, k, value * 2 + 4])
    return data


bar3d = Bar3D()
for _ in range(10):
    bar3d.add(
        "",
        generate_data(),
        shading="lambert",
        xaxis3d_opts=opts.Axis3DOpts(data=x_data, type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(data=y_data, type_="value"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
bar3d.set_global_opts(title_opts=opts.TitleOpts("Bar3D-堆叠柱状图示例"))
bar3d.set_series_opts(**{"stack": "stack"})
put_html(bar3d.render_notebook())

