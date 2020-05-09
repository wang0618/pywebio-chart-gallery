import os
import sys
from os import path
import logging
import re
import json
from shutil import copyfile

here = path.dirname(path.abspath(__file__))

src_dir = path.join(here, 'bokeh')

demo_output_dir = path.join(here, 'demos')
img_output_dir = path.join(here, '..', 'assets', 'bokeh')


def process_item(demo_path, name):
    """复制demo文件和封面图片，返回图片是否为bokeh/sphinx/source/_images/thumbs 文件夹下
    （thumbs封面显示效果比较美观，应靠前显示）

    错误时返回None
    """
    file_path = path.join(src_dir, *demo_path.split('/'))
    if not path.exists(file_path):
        print('File not found:', file_path)
        return
    img_dir = path.join(src_dir, *'sphinx/source/_images'.split('/'))
    img_path = '%s/thumbs/%s_t.png' % (img_dir, name)
    is_thumb = False
    if path.exists(img_path):
        is_thumb = True
    elif path.exists('%s/gallery/%s.png' % (img_dir, name)):
        img_path = '%s/gallery/%s.png' % (img_dir, name)
    else:
        print('Image not found:', name)
        return

    copyfile(file_path, path.join(demo_output_dir, name + '.py'))
    copyfile(img_path, path.join(img_output_dir, name + '.png'))
    return is_thumb


def process(demos):
    """处理demo列表，返回处理完成的demo列表"""
    first_demos = []
    second_demos = []

    for item in demos:
        is_thumb = process_item(item['path'], item['name'])
        if is_thumb:
            first_demos.append(item['name'])
        else:
            second_demos.append(item['name'])

    first_demos.extend(second_demos)
    return first_demos


if __name__ == '__main__':
    os.system('rm -r %s' % demo_output_dir)
    os.system('rm -r %s' % img_output_dir)
    os.mkdir(demo_output_dir)
    os.mkdir(img_output_dir)

    gallery = json.load(open(src_dir + '/sphinx/source/docs/gallery.json'))
    demos = process(gallery['details'])
    json.dump(demos, open(path.join(here, 'inventory.json'), 'w'), indent=4)
