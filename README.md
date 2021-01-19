# [PyWebIO Chart Gallery](https://github.com/wang0618/pywebio-chart-gallery)

[PyWebIO](https://github.com/wang0618/PyWebIO) 支持使用第三方库进行数据可视化

本项目展示了在 PyWebIO 中使用以库进行数据可视化：

 - [bokeh](https://github.com/bokeh/bokeh): 使用Bokeh进行数据可视化 [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=bokeh)
 - [pyecharts](https://github.com/pyecharts/pyecharts): 使用Python创建基于Echarts的图表 [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=pyecharts)
 - [cutecharts.py](https://github.com/cutecharts/cutecharts.py): 创建卡通风格图表 [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=cutecharts)
 - [plotly](https://github.com/plotly/plotly.py/): 非常流行的Python数据可视化库，可以生成高质量的交互式图表 [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=plotly)

## Charts Snapshot
### Bokeh

<p align="center">
    <a href="http://pywebio-charts.demo.wangweimin.site/?app=bokeh">
        <img src="https://raw.githubusercontent.com/wang0618/pywebio-chart-gallery/master/assets/bokeh.png" alt="bokeh demo"/>
    </a>
</p>

### Pyecharts

<p align="center">
    <a href="http://pywebio-charts.demo.wangweimin.site/?app=pyecharts">
        <img src="https://raw.githubusercontent.com/wang0618/pywebio-chart-gallery/master/assets/pyecharts.gif" alt="pyecharts demo"/>
    </a>
</p>


### Cutecharts.py

<p align="center">
    <a href="http://pywebio-charts.demo.wangweimin.site/?app=cutecharts">
        <img src="https://raw.githubusercontent.com/wang0618/pywebio-chart-gallery/master/assets/cutecharts.png" alt="cutecharts demo"/>
    </a>
</p>


### Plotly

<p align="center">
    <a href="http://pywebio-charts.demo.wangweimin.site/?app=plotly">
        <img src="https://raw.githubusercontent.com/wang0618/pywebio-chart-gallery/master/assets/plotly.png" alt="plotly demo"/>
    </a>
</p>


<div></div>

## Run Demo

### 启动demo

```bash
python3 run.py
```

### 重新构建demo

```bash
git submodule update --init --recursive --depth=1
python3 pyecharts_demo/build_demos.py
python3 plotly_demo/build_demos.py
python3 bokeh_demo/build_demos.py
```
