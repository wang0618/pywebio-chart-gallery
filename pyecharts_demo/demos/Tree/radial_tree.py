from pywebio.output import put_html
import asyncio
from aiohttp import TCPConnector, ClientSession

import pyecharts.options as opts
from pyecharts.charts import Tree

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=tree-radial

目前无法实现的功能:

1、
"""


async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()


# 获取官方的数据
data = asyncio.run(
    get_json_data(url="https://echarts.baidu.com/examples/data/asset/data/flare.json")
)

c = (
    Tree()
    .add(
        series_name="",
        data=[data],
        pos_top="18%",
        pos_bottom="14%",
        layout="radial",
        symbol="emptyCircle",
        symbol_size=7,
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove")
    )
    
)

c.width = "100%"
put_html(c.render_notebook())
