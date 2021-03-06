from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_dataset(
        source=[
            ["product", "2015", "2016", "2017"],
            ["Matcha Latte", 43.3, 85.8, 93.7],
            ["Milk Tea", 83.1, 73.4, 55.1],
            ["Cheese Cocoa", 86.4, 65.2, 82.5],
            ["Walnut Brownie", 72.4, 53.9, 39.1],
        ]
    )
    .add_yaxis(series_name="2015", yaxis_data=[])
    .add_yaxis(series_name="2016", yaxis_data=[])
    .add_yaxis(series_name="2017", yaxis_data=[])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Dataset simple bar example"),
        xaxis_opts=opts.AxisOpts(type_="category"),
    )
    
)

c.width = "100%"
put_html(c.render_notebook())
