import re
from os import path

import tornado.ioloop
import tornado.web
from tornado.options import define, options

from cutecharts_demo import cutecharts
from pyecharts_demo import pyecharts
from pywebio import STATIC_PATH
from pywebio.output import put_markdown, set_auto_scroll_bottom
from pywebio.platform.tornado import webio_handler


def index():
    set_auto_scroll_bottom(False)
    readme_file = path.join(path.dirname(__file__), "README.md")
    readme = open(readme_file).read()

    readme = re.sub(r"\[demos\]\(.*?\?pywebio_api=(.+?)\)", r"[demos](./?pywebio_api=\g<1>)", readme)
    cdn = r"https://cdn.jsdelivr.net/gh/wang0618/pywebio-chart-gallery@master"
    readme = re.sub(r"!\[(.+?)\]\(.*?(.+?)\)", r"![\g<1>](%s\g<2>)" % cdn, readme)
    readme = re.sub(r"<div></div>[\s\S]*$", "", readme)

    put_markdown(readme)


if __name__ == "__main__":
    define("port", default=8080, help="run on the given port", type=int)
    tornado.options.parse_command_line()

    application = tornado.web.Application([
        (r"/io", webio_handler(index)),
        (r"/cutecharts", webio_handler(cutecharts)),
        (r"/pyecharts", webio_handler(pyecharts)),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": STATIC_PATH, 'default_filename': 'index.html'})
    ])
    application.listen(port=options.port)
    tornado.ioloop.IOLoop.current().start()
