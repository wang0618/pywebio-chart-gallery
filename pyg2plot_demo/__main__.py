from pywebio import start_server

from . import pyg2plot

if __name__ == '__main__':
    start_server(pyg2plot, debug=True, port=8080)
