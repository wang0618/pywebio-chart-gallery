# [PyWebIO Chart Gallery](https://github.com/wang0618/pywebio-chart-gallery)

[PyWebIO](https://github.com/wang0618/PyWebIO) 支持使用第三方库进行数据可视化

本项目展示了在 PyWebIO 使用以下图表库的方式：

 - [pyecharts](https://github.com/pyecharts/pyecharts): 使用Python创建基于Echarts的图表 [**demos**](http://pywebio-charts.wangweimin.site/?pywebio_api=pyecharts)
 - [cutecharts.py](https://github.com/cutecharts/cutecharts.py): 创建卡通风格图表 [**demos**](http://pywebio-charts.wangweimin.site/?pywebio_api=cutecharts)
 - [plotly](https://github.com/plotly/plotly.py/): 非常流行的Python数据可视化库，可以生成高质量的交互式图表 [**demos**](http://pywebio-charts.wangweimin.site/?pywebio_api=plotly)

## Charts Snapshot
### Pyecharts
![pyecharts](/assets/pyecharts.gif)

### Cutecharts.py
![cutecharts](/assets/cutecharts.png)

### Plotly
![plotly](/assets/plotly.png)

<div></div>

## Run Demo

### 启动全部demo

```bash
python3 run.py
```

### 仅启动部分demo

**启动pyecharts demo**

```bash
python3 pyecharts_demo/build_demos.py
python3 -m pyecharts_demo
```

**启动cutecharts.py demo**

```bash
python3 -m cutecharts_demo
```

**plotly demo**

```bash
python3 -m plotly_demo
```
### 同步 [pyecharts-gallery](https://github.com/pyecharts/pyecharts-gallery)

```bash
git submodule init
python3 pyecharts_demo/build_demos.py
```