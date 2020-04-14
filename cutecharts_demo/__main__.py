from pywebio import start_server

from . import cutecharts

if __name__ == '__main__':
    start_server(cutecharts, debug=True, port=8080)
