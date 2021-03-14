# [PyWebIO Chart Gallery](https://github.com/wang0618/pywebio-chart-gallery)

[PyWebIO](https://github.com/wang0618/PyWebIO) supports for data visualization with the third-party libraries.

This repo shows examples of data visualization using plotly, bokeh, pyecharts and cutcharts in PyWebIO

 - [bokeh](https://github.com/bokeh/bokeh): Use bokeh for data visualization. [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=bokeh)
 - [plotly](https://github.com/plotly/plotly.py/): Interactive, open-source, and browser-based graphing library. [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=plotly)
 - [pyecharts](https://github.com/pyecharts/pyecharts): Create Echarts-based charts in Python. [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=pyecharts)
 - [pyg2plot](https://github.com/hustcc/PyG2Plot): Create G2Plot-based charts in Python. [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=pyg2plot)
 - [cutecharts.py](https://github.com/cutecharts/cutecharts.py): Create a hand drawing style charts. [**demos**](http://pywebio-charts.demo.wangweimin.site/?app=cutecharts)

## Charts Snapshot
### Bokeh

<p align="center">
    <a href="http://pywebio-charts.demo.wangweimin.site/?app=bokeh">
        <img src="https://raw.githubusercontent.com/wang0618/pywebio-chart-gallery/master/assets/bokeh.png" alt="bokeh demo"/>
    </a>
</p>

### Plotly

<p align="center">
    <a href="http://pywebio-charts.demo.wangweimin.site/?app=plotly">
        <img src="https://raw.githubusercontent.com/wang0618/pywebio-chart-gallery/master/assets/plotly.png" alt="plotly demo"/>
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


<div></div>

## Run Demo

### Start demo

```bash
python3 run.py
```

### Rebuild demo

```bash
pip3 install -r requirements.txt -r requirements-dev.txt
git submodule update --init --recursive --depth=1
python3 pyecharts_demo/build_demos.py
python3 plotly_demo/build_demos.py
python3 bokeh_demo/build_demos.py
```
