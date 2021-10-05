from pywebio import start_server

from . import bokehs

if __name__ == '__main__':
    start_server(bokehs, debug=True, port=8080, cdn=False)
