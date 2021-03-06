

#### Load and Process Data Files

```python
import json
import pandas as pd

contour_raw_data = pd.read_json('https://raw.githubusercontent.com/plotly/datasets/master/contour_data.json')
scatter_raw_data = pd.read_json('https://raw.githubusercontent.com/plotly/datasets/master/scatter_data.json')

scatter_data =  scatter_raw_data['Data']

def clean_data(data_in):
    """
    Cleans data in a format which can be conveniently
    used for drawing traces. Takes a dictionary as the
    input, and returns a list in the following format:

    input = {'key': ['a b c']}
    output = [key, [a, b, c]]
    """
    key = list(data_in.keys())[0]
    data_out = [key]
    for i in data_in[key]:
        data_out.append(list(map(float, i.split(' '))))

    return data_out


#Example:
print(clean_data({'L1': ['.03 0.5 0.47','0.4 0.5 0.1']}))
```

#### Create Ternary Scatter Plot:

```put_html
<div>
        
        
            <div id="40e679ce-bb1b-4909-8bd1-34ad8ad52230" class="plotly-graph-div" style="height:100%; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("40e679ce-bb1b-4909-8bd1-34ad8ad52230")) {
                    Plotly.newPlot(
                        '40e679ce-bb1b-4909-8bd1-34ad8ad52230',
                        [{"a": [0.25, 0.0, 0.5, 0.25, 0.0, 0.125, 0.025, 0.025, 0.0, 0.05, 0.125, 0.125, 0.05, 0.0, 0.0, 0.1, 0.175, 0.01, 0.025], "b": [0.4, 1.0, 0.5, 0.4, 0.3, 0.7, 0.625, 0.681, 0.72, 0.6, 0.525, 0.35, 0.425, 0.67, 0.55, 0.47, 0.37, 0.59, 0.525], "c": [0.35, 0.0, 0.0, 0.35, 0.7, 0.175, 0.35, 0.294, 0.28, 0.35, 0.35, 0.525, 0.525, 0.33, 0.45, 0.43, 0.45, 0.4, 0.45], "marker": {"color": "green", "size": 10, "symbol": 100}, "mode": "markers", "text": ["L1", "L1", "L1", "L1", "Lam", "L1", "L1", "L1", "L1", "L1", "L1", "H1", "H1", "H1", "H1", "H1", "H1", "H1", "H1"], "type": "scatterternary"}],
                        {"showlegend": false, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "ternary": {"aaxis": {"linewidth": 2, "min": 0.01, "ticks": "outside", "title": {"text": "X"}}, "baxis": {"linewidth": 2, "min": 0.01, "ticks": "outside", "title": {"text": "W"}}, "caxis": {"linewidth": 2, "min": 0.01, "ticks": "outside", "title": {"text": "S"}}, "sum": 1}, "title": {"text": "Ternary Scatter Plot"}},
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

a_list = []
b_list = []
c_list = []
text = []

for raw_data in scatter_data:
    data = clean_data(raw_data)
    text.append(data[0])
    c_list.append(data[1][0])
    a_list.append(data[1][1])
    b_list.append(data[1][2])

fig = go.Figure(go.Scatterternary(
  text=text,
  a=a_list,
  b=b_list,
  c=c_list,
  mode='markers',
  marker={'symbol': 100,
          'color': 'green',
          'size': 10},
))

fig.update_layout({
    'title': 'Ternary Scatter Plot',
    'ternary':
        {
        'sum':1,
        'aaxis':{'title': 'X', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
        'baxis':{'title': 'W', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
        'caxis':{'title': 'S', 'min': 0.01, 'linewidth':2, 'ticks':'outside' }
    },
    'showlegend': False
})

html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

#### Create Ternary Contour Plot:

```put_html
<div>
        
        
            <div id="53500f87-c686-4265-b262-66ace180b3af" class="plotly-graph-div" style="height:100%; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    
                if (document.getElementById("53500f87-c686-4265-b262-66ace180b3af")) {
                    Plotly.newPlot(
                        '53500f87-c686-4265-b262-66ace180b3af',
                        [{"a": [100.0, 0.0, 0.0, 100.0], "b": [0.0, 100.0, 0.0, 0.0], "c": [0.0, 0.0, 100.0, 0.0], "fill": "toself", "fillcolor": "#8dd3c7", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "two", "type": "scatterternary"}, {"a": [100.0, 95.8870894, 93.05929541, 89.20796877, 86.55389355, 85.0, 100.0], "b": [0.0, 3.407846008, 3.107890932, 2.628178401, 1.670370264, 0.0, 0.0], "c": [0.0, 0.705064593, 3.832813659, 8.163852833, 11.77573619, 15.0, 0.0], "fill": "toself", "fillcolor": "#ffffb3", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "L1", "type": "scatterternary"}, {"a": [83.0, 84.41996886, 85.42572731, 83.15262644, 81.10556114, 78.06950578, 76.02244047, 73.66348601, 72.81367214, 73.0, 83.0], "b": [0.0, 1.639781884, 3.045636224, 4.121486083, 3.761971172, 3.671283982, 3.311769071, 1.815766517, 0.978155999, 0.0, 0.0], "c": [17.0, 13.94024926, 11.52863646, 12.72588747, 15.13246769, 18.25921024, 20.66579045, 24.52074747, 26.20817187, 27.0, 17.0], "fill": "toself", "fillcolor": "#bebada", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "V1", "type": "scatterternary"}, {"a": [71.0, 72.17111383, 73.26373167, 74.23494753, 75.05021882, 76.19515345, 76.50704261, 75.29201699, 71.63117752, 69.46271023, 68.10951423, 65.76732816, 62.43615205, 61.4126194, 59.57381546, 57.99558969, 55.51523324, 54.4226154, 52.30646491, 50.2771738, 48.8548926, 71.0], "b": [0.0, 2.832056541, 3.908984349, 4.866253512, 5.255278854, 5.554694954, 6.691182598, 8.39537509, 8.932491557, 8.453318001, 8.363169786, 8.541849292, 8.989356519, 8.809599064, 8.240816267, 6.685253877, 5.069592677, 3.992664868, 2.735979604, 1.150367809, 0.163049241, 0.0], "c": [29.0, 24.99682963, 22.82728398, 20.89879895, 19.69450233, 18.25015159, 16.80177479, 16.31260792, 19.43633093, 22.08397177, 23.52731599, 25.69082254, 28.57449143, 29.77778154, 32.18536827, 35.31915644, 39.41517408, 41.58471973, 44.95755549, 48.57245839, 50.98205816, 29.0], "fill": "toself", "fillcolor": "#fb8072", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "H1", "type": "scatterternary"}, {"a": [48.28242528, 48.05638972, 46.56401754, 45.21082153, 43.54573637, 44.0, 48.28242528], "b": [0.01334119, 1.44870596, 2.464995984, 2.374847769, 1.14821191, 0.0, 0.01334119], "c": [51.70423353, 50.49490432, 50.97098648, 52.4143307, 55.30605172, 56.51135486, 51.70423353], "fill": "toself", "fillcolor": "#80b1d3", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "V1-bicont", "type": "scatterternary"}, {"a": [39.2088018, 44.60280582, 47.88065935, 53.79380811, 55.02459633, 55.50919847, 55.85563022, 55.57727786, 53.9457295, 51.44659307, 48.60102488, 45.51265273, 43.46558742, 42.19925081, 34.20348835, 31.27206658, 22.25377727, 20.22549196, 19.60171364, 17.98894528, 17.36516696, 17.59120253, 17.5, 39.2088018], "b": [0.189864798, 4.677333487, 7.908116913, 16.22358431, 19.09485282, 22.47426635, 24.05933917, 26.27221565, 28.39494391, 30.90615854, 31.83230035, 32.51912487, 32.15960996, 31.74053521, 25.51774667, 23.87203607, 14.56871113, 10.08232039, 7.809345103, 5.805197537, 3.532222249, 2.096857479, 0.0, 0.189864798], "c": [60.6013334, 50.71986069, 44.21122373, 29.98260759, 25.88055085, 22.01653518, 20.08503061, 18.15050649, 17.65932659, 17.64724839, 19.56667477, 21.96822241, 24.37480262, 26.06021399, 40.27876497, 44.85589736, 63.1775116, 69.69218765, 72.58894125, 76.20585719, 79.10261079, 80.31193999, 82.48752474, 60.6013334], "fill": "toself", "fillcolor": "#fdb462", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "Lam", "type": "scatterternary"}, {"a": [15.68130181, 16.4787989, 17.67504453, 19.02723474, 20.60546051, 21.81948033, 21.87079133, 22.66828842, 19.80595183, 17.68980133, 16.09480716, 14.98542092, 13.78917529, 15.68130181], "b": [6.432462219, 8.047584445, 10.47026778, 13.46119494, 15.01675733, 16.21334379, 18.33661103, 19.95173325, 19.203193, 17.94650773, 14.71626328, 11.96465341, 9.541970076, 6.432462219], "c": [77.88623597, 75.47361666, 71.85468769, 67.51157032, 64.37778216, 61.96717588, 59.79259764, 57.37997833, 60.99085517, 64.36369093, 69.18892955, 73.04992567, 76.66885464, 77.88623597], "fill": "toself", "fillcolor": "#b3de69", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "V2-bicont", "type": "scatterternary"}, {"a": [14.49880719, 15.8509974, 18.6777856, 20.01220161, 21.62496998, 23.48054231, 24.22572261, 24.88404351, 25.78516839, 26.01019816, 26.94586563, 27.23998059, 27.29129158, 26.99516503, 26.73458687, 26.5430939, 25.98739498, 25.57087224, 23.69651992, 22.89902283, 22.10152574, 21.42543064, 20.87073752, 20.40290378, 19.84821066, 19.13757296, 17.88901054, 16.17261438, 13.77911733, 12.08049537, 12.84546145, 12.39640771, 13.24823318, 14.49880719], "b": [14.38679778, 17.37772494, 20.57845896, 24.795483, 26.79963057, 29.04309543, 31.43572936, 34.15728983, 37.11816758, 38.58358176, 41.99304469, 44.35562922, 46.47889645, 49.91786982, 50.90464941, 52.78859936, 54.31357337, 54.73210914, 56.61552011, 55.00039789, 53.38527566, 51.88981208, 50.51400715, 48.80927568, 47.43347074, 45.48942199, 43.84425036, 40.49434726, 38.54975953, 33.97375955, 29.33873871, 23.50713141, 18.54318404, 14.38679778], "c": [71.11439503, 66.77127766, 60.74375545, 55.19231539, 51.57539945, 47.47636226, 44.33854803, 40.95866666, 37.09666403, 35.40622009, 31.06108969, 28.4043902, 26.22981196, 23.08696515, 22.36076372, 20.66830674, 19.69903165, 19.69701862, 19.68795997, 22.10057929, 24.5131986, 26.68475728, 28.61525534, 30.78782054, 32.7183186, 35.37300505, 38.2667391, 43.33303836, 47.67112314, 53.94574509, 57.81579984, 64.09646088, 68.20858278, 71.11439503], "fill": "toself", "fillcolor": "#fccde5", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "H2", "type": "scatterternary"}, {"a": [10.15382625, 12.39137873, 12.6331769, 12.6321711, 13.11677323, 14.12253169, 15.02365656, 16.41038937, 17.39837363, 18.43867468, 18.61138766, 17.96882935, 17.13578387, 15.76481367, 13.45717021, 11.4446475, 10.26517027, 9.172552427, 9.191332419, 9.244655007, 8.881454855, 8.379078525, 8.397858517, 8.641668278, 8.590357283, 10.15382625], "b": [36.63468223, 38.01102614, 41.15112237, 44.05190132, 47.43131485, 48.83716919, 51.79804694, 55.23755928, 57.8695105, 59.72395002, 61.9668759, 63.82077644, 64.65784799, 65.79379666, 66.42106134, 66.5101316, 65.76213033, 64.68520252, 60.55832669, 56.88003603, 53.62028115, 51.46696451, 47.34008868, 44.67862703, 42.55535979, 36.63468223], "c": [53.21149152, 49.59759514, 46.21570073, 43.31592758, 39.45191192, 37.04029912, 33.1782965, 28.35205135, 24.73211587, 21.8373753, 19.42173644, 18.2103942, 18.20636814, 18.44138967, 20.12176845, 22.0452209, 23.9726994, 26.14224506, 30.25034089, 33.87530896, 37.49826399, 40.15395696, 44.2620528, 46.67970469, 48.85428293, 53.21149152], "fill": "toself", "fillcolor": "#d9d9d9", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "V2", "type": "scatterternary"}, {"a": [13.20732567, 0.0, 0.207585708, 1.371300335, 1.795869443, 2.318031561, 2.009159793, 4.441222629, 13.06378078, 13.37365835, 13.78917529, 12.17439533, 10.2990372, 9.586387913, 9.793643486, 9.827180285, 9.930808072, 9.825168693, 9.338554967, 6.942040522, 6.975577322, 7.130516104, 6.609359782, 8.219110762, 8.547768318, 10.1082199, 12.62211314, 12.9340023, 13.33174504, 13.08793528, 13.20732567], "b": [86.48719666, 100.0, 51.70358693, 47.8761272, 24.25135987, 19.37702173, 9.538197253, 0.32825438, 0.121681367, 7.059726902, 9.541970076, 13.3393804, 18.12357032, 21.98107945, 24.67259051, 28.02195463, 29.36771016, 33.82351252, 36.24565689, 43.00340599, 46.35277011, 49.82179288, 51.79535207, 62.50183647, 65.31300618, 68.09466545, 73.05969077, 74.19617842, 77.90451847, 80.56598013, 86.48719666], "c": [0.305477664, 0.0, 48.08882736, 50.75257247, 73.95277069, 78.30494671, 88.45264295, 95.23052299, 86.81453785, 79.56661475, 76.66885464, 74.48622427, 71.57739248, 68.43253264, 65.533766, 62.15086508, 60.70148177, 56.35131878, 54.41578815, 50.05455349, 46.67165257, 43.04769102, 41.59528815, 29.27905277, 26.13922551, 21.79711465, 14.31819609, 12.86981929, 8.763736484, 6.346084591, 0.305477664], "fill": "toself", "fillcolor": "#bc80bd", "line": {"color": "#444", "shape": "spline"}, "mode": "lines", "text": "L2", "type": "scatterternary"}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Ternary Contour Plot"}},
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


contour_dict = contour_raw_data['Data']

# Defining a colormap:
colors = ['#8dd3c7','#ffffb3','#bebada',
          '#fb8072','#80b1d3','#fdb462',
          '#b3de69','#fccde5','#d9d9d9',
          '#bc80bd']
colors_iterator = iter(colors)

fig = go.Figure()

for raw_data in contour_dict:
    data = clean_data(raw_data)

    a = [inner_data[0] for inner_data in data[1:]]
    a.append(data[1][0]) # Closing the loop

    b = [inner_data[1] for inner_data in data[1:]]
    b.append(data[1][1]) # Closing the loop

    c = [inner_data[2] for inner_data in data[1:]]
    c.append(data[1][2]) # Closing the loop

    fig.add_trace(go.Scatterternary(
        text = data[0],
        a=a, b=b, c=c, mode='lines',
        line=dict(color='#444', shape='spline'),
        fill='toself',
        fillcolor = colors_iterator.__next__()
    ))

fig.update_layout(title = 'Ternary Contour Plot')
html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
```

```python

```
