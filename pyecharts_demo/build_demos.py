import os
import sys
from os import path

pyecharts_src_path = path.join(path.dirname(path.abspath(__file__)), "pyecharts-gallery")
sys.path.insert(0, pyecharts_src_path)
from run_all import ChartModelDict

import json
from util import migrate_code
import logging
from shutil import copyfile

inject_code = r"""
import sys
from pyecharts.charts.base import Base
from pyecharts.components import Image,Table
from pyecharts.charts import Page,Tab

def render(self, path: str = "render.html", template_name: str = "simple_chart.html", *args, **kwargs):
    self.width = "100%"
    html = self.render_notebook().__html__()
    open(sys.argv[1], 'w').write(html)
    
Tab.render = Page.render = Table.render = Image.render = Base.render = render
"""


def process_dir(src_dir, target_dir, tmp_file):
    """
    1. 将src_dir文件夹下python脚本转化成对pywebio的调用，保存到 target_dir
    2. 将src_dir文件夹下数据文件复制到 target_dir
    3. 将src_dir文件夹下python脚本对pyecharts render()的调用改为使用render_notebook(), 并输出内容到 target_dir/output
    """
    output_dir = path.join(target_dir, 'output')
    os.mkdir(output_dir)

    for script in os.listdir(src_dir):
        file = path.join(src_dir, script)
        if script.endswith(('.html', '.md')):
            continue
        if not script.endswith('.py'):  # 数据文件
            copyfile(file, path.join(target_dir, script))
            continue

        code = open(file).read()
        try:
            pywebio_code = migrate_code(code)
            open(path.join(target_dir, script), 'w').write(pywebio_code)
        except:
            logging.exception('migrate_code() error in %s', file)
            continue

        with open(tmp_file, 'w') as f:
            f.write(inject_code)
            f.write(code)
        print(f"\tProcessing script {script}")
        script_name = script[:-len(".py")]

        html_path = path.join(output_dir, script_name) + '.html'
        status = os.system("python3 %s %s" % (tmp_file, html_path))
        if int(status) != 0:
            print(f"Error in get output of {file}")
        if not path.exists(html_path):
            print(f"Error in make output of {file}")


def make_pyecharts(output_dir, tmp_file):
    charts = []
    cwd = os.getcwd()
    for name in ChartModelDict.keys():
        print(f"Processing dir {name}")
        dir = path.join(pyecharts_src_path, name)
        os.chdir(dir)

        target_dir = path.join(output_dir, name)
        os.mkdir(target_dir)
        process_dir(dir, target_dir, tmp_file)

    os.chdir(cwd)
    return charts


if __name__ == '__main__':
    file_dir = path.dirname(path.abspath(__file__))

    # 保存demo列表
    inventory_file = path.join(file_dir, 'inventory.json')
    json.dump(list(ChartModelDict.items()), open(inventory_file, 'w'), indent=4, ensure_ascii=False)

    output_dir = path.join(file_dir, "demo")
    # 清空旧demo文件
    os.system(f"rm -rf {output_dir}/*")

    tmp_file = path.join(output_dir, '_tmp.py')
    try:
        make_pyecharts(output_dir, tmp_file)
    finally:
        os.remove(tmp_file)
