from pywebio import start_server

from . import pyecharts

if __name__ == '__main__':
    start_server(pyecharts, port=8080, debug=True, auto_open_webbrowser=False)
