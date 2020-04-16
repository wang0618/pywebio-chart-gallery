

### Basic Carpet Plot

Set the `x` and `y` coorindates, using `x` and `y` attributes. If `x` coorindate values are ommitted a cheater plot will be created. To save parameter values use `a` and `b` attributes. To make changes to the axes, use `aaxis` or `baxis` attributes. For a more detailed list of axes attributes refer to [python reference](https://plotly.com/python/reference/#carpet-aaxis).

```put_html
<div>
        
        
            <div id="801a0e73-eefc-4894-bee0-6b96ea46d636" class="plotly-graph-div" style="height:100%; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("801a0e73-eefc-4894-bee0-6b96ea46d636")) {
                    Plotly.newPlot(
                        '801a0e73-eefc-4894-bee0-6b96ea46d636',
                        [{"a": [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], "aaxis": {"minorgridcount": 9, "smoothing": 0, "tickprefix": "a = ", "type": "linear"}, "b": [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6], "baxis": {"minorgridcount": 9, "smoothing": 0, "tickprefix": "b = ", "type": "linear"}, "type": "carpet", "x": [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5], "y": [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75]}],
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

fig = go.Figure(go.Carpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    x = [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
    y = [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
    aaxis = dict(
        tickprefix = 'a = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    ),
    baxis = dict(
        tickprefix = 'b = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    )
))

html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

### Add Contours

```python inputHidden=false outputHidden=false
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Contourcarpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    z = [1, 1.96, 2.56, 3.0625, 4, 5.0625, 1, 7.5625, 9, 12.25, 15.21, 14.0625],
    autocontour = False,
    contours = dict(
        start = 1,
        end = 14,
        size = 1
    ),
    line = dict(
        width = 2,
        smoothing = 0
    ),
    colorbar = dict(
       len = 0.4,
        y = 0.25
    )
))

fig.add_trace(go.Carpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    x = [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
    y = [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
    aaxis = dict(
        tickprefix = 'a = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    ),
    baxis = dict(
        tickprefix = 'b = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    )
))

fig.show()
```

### Add Multiple Traces

```python inputHidden=false outputHidden=false
import plotly.graph_objects as go
import json
from urllib.request import urlopen

url = "https://raw.githubusercontent.com/bcdunbar/datasets/master/airfoil_data.json"
data = json.load(urlopen(url))


fig=go.Figure()

fig.add_trace(go.Carpet(
    a = data[0]['a'],
    b = data[0]['b'],
    x = data[0]['x'],
    y = data[0]['y'],
    baxis = dict(
      startline = False,
      endline = False,
      showticklabels = "none",
      smoothing = 0,
      showgrid = False
    ),
    aaxis = dict(
      startlinewidth = 2,
      startline = True,
      showticklabels = "none",
      endline = True,
      showgrid = False,
      endlinewidth = 2,
      smoothing = 0
    )
))

fig.add_trace(go.Contourcarpet(
    z = data[1]['z'],
    autocolorscale = False,
    zmax = 1,
    name = "Pressure",
    colorscale = "Viridis",
    zmin = -8,
    colorbar = dict(
      y = 0,
      yanchor = "bottom",
      titleside = "right",
      len = 0.75,
      title = "Pressure coefficient, c<sub>p</sub>"
    ),
    contours = dict(
      start = -1,
      size = 0.025,
      end = 1.000,
      showlines = False
    ),
    line = dict(
      smoothing = 0
    ),
    autocontour = False,
    zauto = False
))

fig.add_trace(go.Contourcarpet(
    z = data[2]['z'],
    opacity = 0.300,
    showlegend = True,
    name = "Streamlines",
    autocontour = True,
    ncontours = 50,
    contours = dict(
      coloring = "none"
    ),
    line = dict(
      color = "white",
      width = 1
    )
))

fig.add_trace(go.Contourcarpet(
    z = data[3]['z'],
    showlegend = True,
    name = "Pressure<br>contours",
    autocontour = False,
    line = dict(
        color = "rgba(0, 0, 0, 0.5)",
        smoothing = 1
    ),
    contours = dict(
        size = 0.250,
        start = -4,
        coloring = "none",
        end = 1.000,
        showlines = True
      )
))

fig.add_trace(go.Scatter(
    x = data[4]['x'],
    y = data[4]['y'],
    legendgroup = "g1",
    name = "Surface<br>pressure",
    mode = "lines",
    hoverinfo = "skip",
    line = dict(
      color = "rgba(255, 0, 0, 0.5)",
      width = 1,
      shape = "spline",
      smoothing = 1
    ),
    fill = "toself",
    fillcolor = "rgba(255, 0, 0, 0.2)"
))

fig.add_trace(go.Scatter(
    x = data[5]['x'],
    y = data[5]['y'],
    showlegend = False,
    legendgroup = "g1",
    mode = "lines",
    hoverinfo = "skip",
    line = dict(
      color = "rgba(255, 0, 0, 0.3)",
      width = 1
    )
))

fig.add_trace(go.Scatter(
    x = data[6]['x'],
    y = data[6]['y'],
    showlegend = False,
    legendgroup = "g1",
    name = "cp",
    text = data[6]['text'],
    hoverinfo = "text",
    mode = "lines",
    line = dict(
      color = "rgba(255, 0, 0, 0.2)",
      width = 0
    )
))

fig.update_layout(
    yaxis = dict(
      zeroline = False,
      range = [-1.800,1.800],
      showgrid = False
    ),
    dragmode = "pan",
    height = 700,
    xaxis = dict(
      zeroline = False,
      scaleratio = 1,
      scaleanchor = 'y',
      range = [-3.800,3.800],
      showgrid = False
    ),
    title = "Flow over a Karman-Trefftz airfoil",
    hovermode = "closest",
    margin = dict(
      r = 60,
      b = 40,
      l = 40,
      t = 80
    ),
    width = 900
)

fig.show()
```

### Reference

See https://plotly.com/python/reference/#contourcarpet for more information and chart attribute options!
