from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import TreeMap

data = [
    {"value": 40, "name": "我是A"},
    {
        "value": 180,
        "name": "我是B",
        "children": [
            {
                "value": 76,
                "name": "我是B.children",
                "children": [
                    {"value": 12, "name": "我是B.children.a"},
                    {"value": 28, "name": "我是B.children.b"},
                    {"value": 20, "name": "我是B.children.c"},
                    {"value": 16, "name": "我是B.children.d"},
                ],
            }
        ],
    },
]

c = (
    TreeMap()
    .add("演示数据", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-基本示例"))
    
)

c.width = "100%"
put_html(c.render_notebook())
