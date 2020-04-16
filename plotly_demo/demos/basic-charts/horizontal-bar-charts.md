

See more examples of bar charts (including vertical bar charts) and styling options [here](https://plotly.com/python/bar-charts/).

### Horizontal Bar Chart with Plotly Express

[Plotly Express](https://plotly.com/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](https://plotly.com/python/px-arguments/) and produces [easy-to-style figures](https://plotly.com/python/styling-plotly-express/). For a horizontal bar char, use the `px.bar` function with `orientation='h'`.

#### Basic Horizontal Bar Chart with Plotly Express

```put_html
<div>
        
        
            <div id="59ebfd91-2745-4288-aff7-31a9598eb51c" class="plotly-graph-div" style="height:100%; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("59ebfd91-2745-4288-aff7-31a9598eb51c")) {
                    Plotly.newPlot(
                        '59ebfd91-2745-4288-aff7-31a9598eb51c',
                        [{"alignmentgroup": "True", "hovertemplate": "total_bill=%{x}<br>day=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "h", "showlegend": false, "textposition": "auto", "type": "bar", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "xaxis": "x", "y": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur"], "yaxis": "y"}],
                        {"barmode": "relative", "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "day"}}},
                        {"responsive": true}
                    )
                };
                });
            </script>
        </div>
```

```python
from pywebio.output import put_html
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="total_bill", y="day", orientation='h')
html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

#### Configure horizontal bar chart

In this example a column is used to color the bars, and we add the information from other columns to the hover data.

```put_html
<div>
        
        
            <div id="472447e2-a191-4f85-88a7-ad9d49085628" class="plotly-graph-div" style="height:400px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("472447e2-a191-4f85-88a7-ad9d49085628")) {
                    Plotly.newPlot(
                        '472447e2-a191-4f85-88a7-ad9d49085628',
                        [{"alignmentgroup": "True", "customdata": [[1.01, 2.0], [1.66, 3.0], [3.5, 3.0], [3.31, 2.0], [3.61, 4.0], [4.71, 4.0], [2.0, 2.0], [3.12, 4.0], [1.96, 2.0], [3.23, 2.0], [1.71, 2.0], [5.0, 4.0], [1.57, 2.0], [3.0, 4.0], [3.02, 2.0], [3.92, 2.0], [1.67, 3.0], [3.71, 3.0], [3.5, 3.0], [2.54, 2.0], [3.06, 2.0], [1.32, 2.0], [5.6, 4.0], [3.0, 2.0], [5.0, 2.0], [6.0, 4.0], [2.05, 3.0], [3.0, 2.0], [2.5, 2.0], [2.6, 2.0], [5.2, 4.0], [1.56, 2.0], [4.34, 4.0], [3.51, 2.0], [4.0, 3.0], [2.55, 2.0], [4.0, 3.0], [3.5, 2.0], [5.07, 4.0], [2.5, 2.0], [2.0, 2.0], [2.74, 3.0], [2.0, 4.0], [2.0, 4.0], [5.14, 5.0], [5.0, 6.0], [3.75, 4.0], [2.61, 2.0], [2.0, 4.0], [3.5, 4.0], [2.5, 2.0], [2.0, 3.0], [2.0, 2.0], [3.0, 2.0], [3.48, 3.0], [2.24, 2.0], [4.5, 4.0], [5.15, 2.0], [3.18, 2.0], [4.0, 2.0], [3.11, 2.0], [2.0, 2.0], [2.0, 2.0], [4.0, 2.0], [3.55, 2.0], [3.68, 4.0], [5.65, 2.0], [3.5, 3.0], [6.5, 4.0], [3.0, 2.0], [5.0, 5.0], [3.5, 3.0], [2.0, 5.0], [3.5, 3.0], [4.0, 3.0], [1.5, 2.0]], "hovertemplate": "day=Sun<br>total_bill=%{x}<br>sex=%{y}<br>tip=%{customdata[0]}<br>size=%{customdata[1]}<extra></extra>", "legendgroup": "Sun", "marker": {"color": "#636efa"}, "name": "Sun", "offsetgroup": "Sun", "orientation": "h", "showlegend": true, "textposition": "auto", "type": "bar", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.07, 23.95, 25.71, 17.31, 29.93, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69], "xaxis": "x", "y": ["Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male"], "yaxis": "y"}, {"alignmentgroup": "True", "customdata": [[3.35, 3.0], [4.08, 2.0], [2.75, 2.0], [2.23, 2.0], [7.58, 4.0], [3.18, 2.0], [2.34, 4.0], [2.0, 2.0], [2.0, 2.0], [4.3, 2.0], [3.0, 2.0], [1.45, 2.0], [2.5, 4.0], [3.0, 2.0], [2.45, 4.0], [3.27, 2.0], [3.6, 3.0], [2.0, 3.0], [3.07, 3.0], [2.31, 3.0], [5.0, 3.0], [2.24, 3.0], [3.0, 4.0], [1.5, 2.0], [1.76, 2.0], [6.73, 4.0], [3.21, 2.0], [2.0, 2.0], [1.98, 2.0], [3.76, 4.0], [2.64, 3.0], [3.15, 3.0], [2.47, 2.0], [1.0, 1.0], [2.01, 2.0], [2.09, 2.0], [1.97, 2.0], [3.0, 3.0], [3.14, 2.0], [5.0, 2.0], [2.2, 2.0], [1.25, 2.0], [3.08, 2.0], [2.5, 3.0], [3.48, 2.0], [4.08, 2.0], [1.64, 2.0], [4.06, 2.0], [4.29, 2.0], [3.76, 2.0], [4.0, 2.0], [3.0, 2.0], [1.0, 1.0], [1.61, 2.0], [2.0, 2.0], [10.0, 3.0], [3.16, 2.0], [3.41, 3.0], [3.0, 4.0], [2.03, 2.0], [2.23, 2.0], [2.0, 3.0], [5.16, 4.0], [9.0, 4.0], [2.5, 2.0], [6.5, 3.0], [1.1, 2.0], [3.0, 5.0], [1.5, 2.0], [1.44, 2.0], [3.09, 4.0], [3.0, 4.0], [2.72, 2.0], [2.88, 2.0], [2.0, 4.0], [3.0, 3.0], [3.39, 2.0], [1.47, 2.0], [3.0, 2.0], [1.25, 2.0], [1.0, 2.0], [1.17, 2.0], [4.67, 3.0], [5.92, 3.0], [2.0, 2.0], [2.0, 2.0], [1.75, 2.0]], "hovertemplate": "day=Sat<br>total_bill=%{x}<br>sex=%{y}<br>tip=%{customdata[0]}<br>size=%{customdata[1]}<extra></extra>", "legendgroup": "Sat", "marker": {"color": "#EF553B"}, "name": "Sat", "offsetgroup": "Sat", "orientation": "h", "showlegend": true, "textposition": "auto", "type": "bar", "x": [20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 10.59, 10.63, 50.81, 15.81, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82], "xaxis": "x", "y": ["Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male"], "yaxis": "y"}, {"alignmentgroup": "True", "customdata": [[4.0, 4.0], [3.0, 2.0], [2.71, 2.0], [3.0, 2.0], [3.4, 2.0], [1.83, 1.0], [5.0, 2.0], [2.03, 2.0], [5.17, 4.0], [2.0, 2.0], [4.0, 2.0], [5.85, 2.0], [3.0, 2.0], [1.5, 2.0], [1.8, 2.0], [2.92, 4.0], [2.31, 2.0], [1.68, 2.0], [2.5, 2.0], [2.0, 2.0], [2.52, 2.0], [4.2, 6.0], [1.48, 2.0], [2.0, 2.0], [2.0, 2.0], [2.18, 3.0], [1.5, 2.0], [2.83, 2.0], [1.5, 2.0], [2.0, 2.0], [3.25, 2.0], [1.25, 2.0], [2.0, 2.0], [2.0, 2.0], [2.0, 2.0], [2.75, 2.0], [3.5, 2.0], [6.7, 6.0], [5.0, 5.0], [5.0, 6.0], [2.3, 2.0], [1.5, 2.0], [1.36, 3.0], [1.63, 2.0], [1.73, 2.0], [2.0, 2.0], [4.19, 2.0], [2.56, 2.0], [2.02, 2.0], [4.0, 2.0], [1.44, 2.0], [2.0, 2.0], [5.0, 4.0], [2.0, 2.0], [2.0, 2.0], [4.0, 3.0], [2.01, 2.0], [2.0, 2.0], [2.5, 2.0], [4.0, 4.0], [3.23, 3.0], [3.0, 2.0]], "hovertemplate": "day=Thur<br>total_bill=%{x}<br>sex=%{y}<br>tip=%{customdata[0]}<br>size=%{customdata[1]}<extra></extra>", "legendgroup": "Thur", "marker": {"color": "#00cc96"}, "name": "Thur", "offsetgroup": "Thur", "orientation": "h", "showlegend": true, "textposition": "auto", "type": "bar", "x": [27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 18.78], "xaxis": "x", "y": ["Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Male", "Female", "Female"], "yaxis": "y"}, {"alignmentgroup": "True", "customdata": [[3.0, 2.0], [3.5, 2.0], [1.0, 2.0], [4.3, 2.0], [3.25, 2.0], [4.73, 4.0], [4.0, 2.0], [1.5, 2.0], [3.0, 2.0], [1.5, 2.0], [2.5, 2.0], [3.0, 2.0], [2.2, 2.0], [3.48, 2.0], [1.92, 1.0], [3.0, 3.0], [1.58, 2.0], [2.5, 2.0], [2.0, 2.0]], "hovertemplate": "day=Fri<br>total_bill=%{x}<br>sex=%{y}<br>tip=%{customdata[0]}<br>size=%{customdata[1]}<extra></extra>", "legendgroup": "Fri", "marker": {"color": "#ab63fa"}, "name": "Fri", "offsetgroup": "Fri", "orientation": "h", "showlegend": true, "textposition": "auto", "type": "bar", "x": [28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09], "xaxis": "x", "y": ["Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Female"], "yaxis": "y"}],
                        {"barmode": "relative", "height": 400, "legend": {"title": {"text": "day"}, "tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Restaurant bills"}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "sex"}}},
                        {"responsive": true}
                    )
                };
                });
            </script>
        </div>
```

```python
from pywebio.output import put_html
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="total_bill", y="sex", color='day', orientation='h',
             hover_data=["tip", "size"],
             height=400,
             title='Restaurant bills')
html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

### Horizontal Bar Chart with go.Bar

When data are not available as a tidy dataframe, you can use the more generic function `go.Bar` from `plotly.graph_objects`. All the options of `go.Bar` are documented in the reference https://plotly.com/python/reference/#bar

#### Basic Horizontal Bar Chart

```put_html
<div>
        
        
            <div id="58b0c371-13bf-4fbf-85bb-1127751cb75e" class="plotly-graph-div" style="height:100%; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("58b0c371-13bf-4fbf-85bb-1127751cb75e")) {
                    Plotly.newPlot(
                        '58b0c371-13bf-4fbf-85bb-1127751cb75e',
                        [{"orientation": "h", "type": "bar", "x": [20, 14, 23], "y": ["giraffes", "orangutans", "monkeys"]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}},
                        {"responsive": true}
                    )
                };
                });
            </script>
        </div>
```

```python
from pywebio.output import put_html
import plotly.graph_objects as go

fig = go.Figure(go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation='h'))

html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

### Colored Horizontal Bar Chart

```put_html
<div>
        
        
            <div id="3da31a91-8fb9-4d2d-994c-fd0a527af0b3" class="plotly-graph-div" style="height:100%; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("3da31a91-8fb9-4d2d-994c-fd0a527af0b3")) {
                    Plotly.newPlot(
                        '3da31a91-8fb9-4d2d-994c-fd0a527af0b3',
                        [{"marker": {"color": "rgba(246, 78, 139, 0.6)", "line": {"color": "rgba(246, 78, 139, 1.0)", "width": 3}}, "name": "SF Zoo", "orientation": "h", "type": "bar", "x": [20, 14, 23], "y": ["giraffes", "orangutans", "monkeys"]}, {"marker": {"color": "rgba(58, 71, 80, 0.6)", "line": {"color": "rgba(58, 71, 80, 1.0)", "width": 3}}, "name": "LA Zoo", "orientation": "h", "type": "bar", "x": [12, 18, 29], "y": ["giraffes", "orangutans", "monkeys"]}],
                        {"barmode": "stack", "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}},
                        {"responsive": true}
                    )
                };
                });
            </script>
        </div>
```

```python
from pywebio.output import put_html
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(
    y=['giraffes', 'orangutans', 'monkeys'],
    x=[20, 14, 23],
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
fig.add_trace(go.Bar(
    y=['giraffes', 'orangutans', 'monkeys'],
    x=[12, 18, 29],
    name='LA Zoo',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))

fig.update_layout(barmode='stack')
html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

### Color Palette for Bar Chart

```put_html
<div>
        
        
            <div id="8ad3da9b-6a8a-47cf-9e0b-ed64d534dcfc" class="plotly-graph-div" style="height:100%; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("8ad3da9b-6a8a-47cf-9e0b-ed64d534dcfc")) {
                    Plotly.newPlot(
                        '8ad3da9b-6a8a-47cf-9e0b-ed64d534dcfc',
                        [{"marker": {"color": "rgba(38, 24, 74, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [21], "y": ["The course was effectively<br>organized"]}, {"marker": {"color": "rgba(38, 24, 74, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [24], "y": ["The course developed my<br>abilities and skills for<br>the subject"]}, {"marker": {"color": "rgba(38, 24, 74, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [27], "y": ["The course developed my<br>ability to think critically about<br>the subject"]}, {"marker": {"color": "rgba(38, 24, 74, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [29], "y": ["I would recommend this<br>course to a friend"]}, {"marker": {"color": "rgba(71, 58, 131, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [30], "y": ["The course was effectively<br>organized"]}, {"marker": {"color": "rgba(71, 58, 131, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [31], "y": ["The course developed my<br>abilities and skills for<br>the subject"]}, {"marker": {"color": "rgba(71, 58, 131, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [26], "y": ["The course developed my<br>ability to think critically about<br>the subject"]}, {"marker": {"color": "rgba(71, 58, 131, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [24], "y": ["I would recommend this<br>course to a friend"]}, {"marker": {"color": "rgba(122, 120, 168, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [21], "y": ["The course was effectively<br>organized"]}, {"marker": {"color": "rgba(122, 120, 168, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [19], "y": ["The course developed my<br>abilities and skills for<br>the subject"]}, {"marker": {"color": "rgba(122, 120, 168, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [23], "y": ["The course developed my<br>ability to think critically about<br>the subject"]}, {"marker": {"color": "rgba(122, 120, 168, 0.8)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [15], "y": ["I would recommend this<br>course to a friend"]}, {"marker": {"color": "rgba(164, 163, 204, 0.85)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [16], "y": ["The course was effectively<br>organized"]}, {"marker": {"color": "rgba(164, 163, 204, 0.85)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [15], "y": ["The course developed my<br>abilities and skills for<br>the subject"]}, {"marker": {"color": "rgba(164, 163, 204, 0.85)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [11], "y": ["The course developed my<br>ability to think critically about<br>the subject"]}, {"marker": {"color": "rgba(164, 163, 204, 0.85)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [18], "y": ["I would recommend this<br>course to a friend"]}, {"marker": {"color": "rgba(190, 192, 213, 1)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [12], "y": ["The course was effectively<br>organized"]}, {"marker": {"color": "rgba(190, 192, 213, 1)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [11], "y": ["The course developed my<br>abilities and skills for<br>the subject"]}, {"marker": {"color": "rgba(190, 192, 213, 1)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [13], "y": ["The course developed my<br>ability to think critically about<br>the subject"]}, {"marker": {"color": "rgba(190, 192, 213, 1)", "line": {"color": "rgb(248, 248, 249)", "width": 1}}, "orientation": "h", "type": "bar", "x": [14], "y": ["I would recommend this<br>course to a friend"]}],
                        {"annotations": [{"align": "right", "font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "The course was effectively<br>organized", "x": 0.14, "xanchor": "right", "xref": "paper", "y": "The course was effectively<br>organized", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "21%", "x": 10.5, "xref": "x", "y": "The course was effectively<br>organized", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "30%", "x": 36.0, "xref": "x", "y": "The course was effectively<br>organized", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "21%", "x": 61.5, "xref": "x", "y": "The course was effectively<br>organized", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "16%", "x": 80.0, "xref": "x", "y": "The course was effectively<br>organized", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "12%", "x": 94.0, "xref": "x", "y": "The course was effectively<br>organized", "yref": "y"}, {"align": "right", "font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "The course developed my<br>abilities and skills for<br>the subject", "x": 0.14, "xanchor": "right", "xref": "paper", "y": "The course developed my<br>abilities and skills for<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "24%", "x": 12.0, "xref": "x", "y": "The course developed my<br>abilities and skills for<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "31%", "x": 39.5, "xref": "x", "y": "The course developed my<br>abilities and skills for<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "19%", "x": 64.5, "xref": "x", "y": "The course developed my<br>abilities and skills for<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "15%", "x": 81.5, "xref": "x", "y": "The course developed my<br>abilities and skills for<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "11%", "x": 94.5, "xref": "x", "y": "The course developed my<br>abilities and skills for<br>the subject", "yref": "y"}, {"align": "right", "font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "The course developed my<br>ability to think critically about<br>the subject", "x": 0.14, "xanchor": "right", "xref": "paper", "y": "The course developed my<br>ability to think critically about<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "27%", "x": 13.5, "xref": "x", "y": "The course developed my<br>ability to think critically about<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "26%", "x": 40.0, "xref": "x", "y": "The course developed my<br>ability to think critically about<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "23%", "x": 64.5, "xref": "x", "y": "The course developed my<br>ability to think critically about<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "11%", "x": 81.5, "xref": "x", "y": "The course developed my<br>ability to think critically about<br>the subject", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "13%", "x": 93.5, "xref": "x", "y": "The course developed my<br>ability to think critically about<br>the subject", "yref": "y"}, {"align": "right", "font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "I would recommend this<br>course to a friend", "x": 0.14, "xanchor": "right", "xref": "paper", "y": "I would recommend this<br>course to a friend", "yref": "y"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "29%", "x": 14.5, "xref": "x", "y": "I would recommend this<br>course to a friend", "yref": "y"}, {"font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "Strongly<br>agree", "x": 14.5, "xref": "x", "y": 1.1, "yref": "paper"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "24%", "x": 41.0, "xref": "x", "y": "I would recommend this<br>course to a friend", "yref": "y"}, {"font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "Agree", "x": 41.0, "xref": "x", "y": 1.1, "yref": "paper"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "15%", "x": 60.5, "xref": "x", "y": "I would recommend this<br>course to a friend", "yref": "y"}, {"font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "Neutral", "x": 60.5, "xref": "x", "y": 1.1, "yref": "paper"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "18%", "x": 77.0, "xref": "x", "y": "I would recommend this<br>course to a friend", "yref": "y"}, {"font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "Disagree", "x": 77.0, "xref": "x", "y": 1.1, "yref": "paper"}, {"font": {"color": "rgb(248, 248, 255)", "family": "Arial", "size": 14}, "showarrow": false, "text": "14%", "x": 93.0, "xref": "x", "y": "I would recommend this<br>course to a friend", "yref": "y"}, {"font": {"color": "rgb(67, 67, 67)", "family": "Arial", "size": 14}, "showarrow": false, "text": "Strongly<br>disagree", "x": 93.0, "xref": "x", "y": 1.1, "yref": "paper"}], "barmode": "stack", "margin": {"b": 80, "l": 120, "r": 10, "t": 140}, "paper_bgcolor": "rgb(248, 248, 255)", "plot_bgcolor": "rgb(248, 248, 255)", "showlegend": false, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"domain": [0.15, 1], "showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}},
                        {"responsive": true}
                    )
                };
                });
            </script>
        </div>
```

```python
from pywebio.output import put_html
import plotly.graph_objects as go

top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
              'Strongly<br>disagree']

colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)',
          'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
          'rgba(190, 192, 213, 1)']

x_data = [[21, 30, 21, 16, 12],
          [24, 31, 19, 15, 11],
          [27, 26, 23, 11, 13],
          [29, 24, 15, 18, 14]]

y_data = ['The course was effectively<br>organized',
          'The course developed my<br>abilities and skills ' +
          'for<br>the subject', 'The course developed ' +
          'my<br>ability to think critically about<br>the subject',
          'I would recommend this<br>course to a friend']

fig = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=80),
    showlegend=False,
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=14,
                                      color='rgb(67, 67, 67)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations)

html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

### Bar Chart with Line Plot

```put_html
<div>
        
        
            <div id="417e595c-82ef-4f0d-a16d-ac464d09ae81" class="plotly-graph-div" style="height:100%; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("417e595c-82ef-4f0d-a16d-ac464d09ae81")) {
                    Plotly.newPlot(
                        '417e595c-82ef-4f0d-a16d-ac464d09ae81',
                        [{"marker": {"color": "rgba(50, 171, 96, 0.6)", "line": {"color": "rgba(50, 171, 96, 1.0)", "width": 1}}, "name": "Household savings, percentage of household disposable income", "orientation": "h", "type": "bar", "x": [1.3586, 2.2623, 4.9822, 6.5097, 7.4812, 7.5133, 15.2148, 17.5205], "xaxis": "x", "y": ["Japan", "United Kingdom", "Canada", "Netherlands", "United States", "Belgium", "Sweden", "Switzerland"], "yaxis": "y"}, {"line": {"color": "rgb(128, 0, 128)"}, "mode": "lines+markers", "name": "Household net worth, Million USD/capita", "type": "scatter", "x": [93453.92, 81666.57, 69889.62, 78381.53, 141395.3, 92969.02, 66090.18, 122379.3], "xaxis": "x2", "y": ["Japan", "United Kingdom", "Canada", "Netherlands", "United States", "Belgium", "Sweden", "Switzerland"], "yaxis": "y2"}],
                        {"annotations": [{"font": {"color": "rgb(128, 0, 128)", "family": "Arial", "size": 12}, "showarrow": false, "text": "93,454.0M", "x": 73454.0, "xref": "x2", "y": "Japan", "yref": "y2"}, {"font": {"color": "rgb(50, 171, 96)", "family": "Arial", "size": 12}, "showarrow": false, "text": "1.36%", "x": 4.36, "xref": "x", "y": "Japan", "yref": "y"}, {"font": {"color": "rgb(128, 0, 128)", "family": "Arial", "size": 12}, "showarrow": false, "text": "81,667.0M", "x": 61667.0, "xref": "x2", "y": "United Kingdom", "yref": "y2"}, {"font": {"color": "rgb(50, 171, 96)", "family": "Arial", "size": 12}, "showarrow": false, "text": "2.26%", "x": 5.26, "xref": "x", "y": "United Kingdom", "yref": "y"}, {"font": {"color": "rgb(128, 0, 128)", "family": "Arial", "size": 12}, "showarrow": false, "text": "69,890.0M", "x": 49890.0, "xref": "x2", "y": "Canada", "yref": "y2"}, {"font": {"color": "rgb(50, 171, 96)", "family": "Arial", "size": 12}, "showarrow": false, "text": "4.98%", "x": 7.98, "xref": "x", "y": "Canada", "yref": "y"}, {"font": {"color": "rgb(128, 0, 128)", "family": "Arial", "size": 12}, "showarrow": false, "text": "78,382.0M", "x": 58382.0, "xref": "x2", "y": "Netherlands", "yref": "y2"}, {"font": {"color": "rgb(50, 171, 96)", "family": "Arial", "size": 12}, "showarrow": false, "text": "6.51%", "x": 9.51, "xref": "x", "y": "Netherlands", "yref": "y"}, {"font": {"color": "rgb(128, 0, 128)", "family": "Arial", "size": 12}, "showarrow": false, "text": "141,395.0M", "x": 121395.0, "xref": "x2", "y": "United States", "yref": "y2"}, {"font": {"color": "rgb(50, 171, 96)", "family": "Arial", "size": 12}, "showarrow": false, "text": "7.48%", "x": 10.48, "xref": "x", "y": "United States", "yref": "y"}, {"font": {"color": "rgb(128, 0, 128)", "family": "Arial", "size": 12}, "showarrow": false, "text": "92,969.0M", "x": 72969.0, "xref": "x2", "y": "Belgium", "yref": "y2"}, {"font": {"color": "rgb(50, 171, 96)", "family": "Arial", "size": 12}, "showarrow": false, "text": "7.51%", "x": 10.51, "xref": "x", "y": "Belgium", "yref": "y"}, {"font": {"color": "rgb(128, 0, 128)", "family": "Arial", "size": 12}, "showarrow": false, "text": "66,090.0M", "x": 46090.0, "xref": "x2", "y": "Sweden", "yref": "y2"}, {"font": {"color": "rgb(50, 171, 96)", "family": "Arial", "size": 12}, "showarrow": false, "text": "15.21%", "x": 18.21, "xref": "x", "y": "Sweden", "yref": "y"}, {"font": {"color": "rgb(128, 0, 128)", "family": "Arial", "size": 12}, "showarrow": false, "text": "122,379.0M", "x": 102379.0, "xref": "x2", "y": "Switzerland", "yref": "y2"}, {"font": {"color": "rgb(50, 171, 96)", "family": "Arial", "size": 12}, "showarrow": false, "text": "17.52%", "x": 20.52, "xref": "x", "y": "Switzerland", "yref": "y"}, {"font": {"color": "rgb(150,150,150)", "family": "Arial", "size": 10}, "showarrow": false, "text": "OECD \"(2015), Household savings (indicator), Household net worth (indicator). doi: 10.1787/cfc6f499-en (Accessed on 05 June 2015)", "x": -0.2, "xref": "paper", "y": -0.109, "yref": "paper"}], "legend": {"font": {"size": 10}, "x": 0.029, "y": 1.038}, "margin": {"b": 70, "l": 100, "r": 20, "t": 70}, "paper_bgcolor": "rgb(248, 248, 255)", "plot_bgcolor": "rgb(248, 248, 255)", "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Household savings & net worth for eight OECD countries"}, "xaxis": {"anchor": "y", "domain": [0, 0.42], "showgrid": true, "showline": false, "showticklabels": true, "zeroline": false}, "xaxis2": {"anchor": "y2", "domain": [0.47, 1], "dtick": 25000, "showgrid": true, "showline": false, "showticklabels": true, "side": "top", "zeroline": false}, "yaxis": {"anchor": "x", "domain": [0, 0.85], "showgrid": false, "showline": false, "showticklabels": true}, "yaxis2": {"anchor": "x2", "domain": [0, 0.85], "linecolor": "rgba(102, 102, 102, 0.8)", "linewidth": 2, "showgrid": false, "showline": true, "showticklabels": false}},
                        {"responsive": true}
                    )
                };
                });
            </script>
        </div>
```

```python
from pywebio.output import put_html
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

y_saving = [1.3586, 2.2623000000000002, 4.9821999999999997, 6.5096999999999996,
            7.4812000000000003, 7.5133000000000001, 15.2148, 17.520499999999998
            ]
y_net_worth = [93453.919999999998, 81666.570000000007, 69889.619999999995,
               78381.529999999999, 141395.29999999999, 92969.020000000004,
               66090.179999999993, 122379.3]
x = ['Japan', 'United Kingdom', 'Canada', 'Netherlands',
     'United States', 'Belgium', 'Sweden', 'Switzerland']


# Creating two subplots
fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                    shared_yaxes=False, vertical_spacing=0.001)

fig.append_trace(go.Bar(
    x=y_saving,
    y=x,
    marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='Household savings, percentage of household disposable income',
    orientation='h',
), 1, 1)

fig.append_trace(go.Scatter(
    x=y_net_worth, y=x,
    mode='lines+markers',
    line_color='rgb(128, 0, 128)',
    name='Household net worth, Million USD/capita',
), 1, 2)

fig.update_layout(
    title='Household savings & net worth for eight OECD countries',
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
    ),
    yaxis2=dict(
        showgrid=False,
        showline=True,
        showticklabels=False,
        linecolor='rgba(102, 102, 102, 0.8)',
        linewidth=2,
        domain=[0, 0.85],
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 0.42],
    ),
    xaxis2=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0.47, 1],
        side='top',
        dtick=25000,
    ),
    legend=dict(x=0.029, y=1.038, font_size=10),
    margin=dict(l=100, r=20, t=70, b=70),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
)

annotations = []

y_s = np.round(y_saving, decimals=2)
y_nw = np.rint(y_net_worth)

# Adding labels
for ydn, yd, xd in zip(y_nw, y_s, x):
    # labeling the scatter savings
    annotations.append(dict(xref='x2', yref='y2',
                            y=xd, x=ydn - 20000,
                            text='{:,}'.format(ydn) + 'M',
                            font=dict(family='Arial', size=12,
                                      color='rgb(128, 0, 128)'),
                            showarrow=False))
    # labeling the bar net worth
    annotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd + 3,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=12,
                                      color='rgb(50, 171, 96)'),
                            showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper',
                        x=-0.2, y=-0.109,
                        text='OECD "' +
                             '(2015), Household savings (indicator), ' +
                             'Household net worth (indicator). doi: ' +
                             '10.1787/cfc6f499-en (Accessed on 05 June 2015)',
                        font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
                        showarrow=False))

fig.update_layout(annotations=annotations)

html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

### Reference

See more examples of bar charts and styling options [here](https://plotly.com/python/bar-charts/).<br> See https://plotly.com/python/reference/#bar for more information and chart attribute options!
