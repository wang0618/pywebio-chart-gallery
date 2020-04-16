from pywebio import start_server

from . import plotly_demo

if __name__ == '__main__':
    start_server(plotly_demo, debug=True, port=8080)
