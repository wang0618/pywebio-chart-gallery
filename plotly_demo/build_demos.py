import os
import sys
from os import path
import logging
from inventory import all_demos
import re

here = path.dirname(path.abspath(__file__))

src_dir = path.join(here, 'plotly', 'doc', 'python')

plotly_doc_url = "https://plotly.com/"


def build_md(md):
    # 去除顶部注释
    md = re.sub(r"---[\s\S]*?---", "", md)

    # 相对链接转为绝对链接
    md = re.sub(r"([^!])\[(.*?)\]\(/(.*?)\)", r"\g<1>[\g<2>](%s\g<3>)" % plotly_doc_url, md)

    res_md = []
    parts = re.split(r"(```python[\s\S]*?```)", md)

    used_pywebio = False
    for part in parts:
        if not part.startswith('```python'):
            res_md.append(part)
            continue

        code = part[len("```python"):-3].strip()

        if "fig.show()" not in part:
            res_md.append(part)
            try:
                exec(code, locals(), locals())
            except:
                pass
            continue

        # 替换 显示图表调用
        code = code.replace("fig.show()", 'html = fig.to_html(include_plotlyjs="require", full_html=False)')

        # 将生成的html加入md
        try:
            # https://stackoverflow.com/questions/29979313/python-weird-nameerror-name-is-not-defined-in-an-exec-environment
            exec(code, locals(), locals())
            res_md.append('```put_html\n%s\n```\n' % locals()['html'])
        except:
            logging.exception('exec error')
            res_md.append(part)
            continue
            # print(code[:300])
            # return False

        # 将代码加入md
        res_md.append('\n```python\nfrom pywebio.output import put_html\n%s\nput_html(html)\n```' % code)
        used_pywebio = True

    if not used_pywebio:
        return False

    return ''.join(res_md)


def build_dir(names, src_dir, outout_dir):
    for name in names:
        md_file = path.join(src_dir, name + '.md')
        print("\t%s" % md_file)
        md = open(md_file).read()
        new_md = build_md(md)
        if not new_md:
            continue
        open(path.join(outout_dir, name + '.md'), 'w').write(new_md)


if __name__ == '__main__':
    demos_dir = path.join(here, 'demos')
    os.system('rm -rf %s/*' % demos_dir)
    for chapter, contents in all_demos.items():
        chapter_dir = chapter.replace(" ", "-").lower()
        chapter_path = path.join(demos_dir, chapter_dir)
        os.mkdir(chapter_path)
        print(chapter_path)
        build_dir(contents.keys(), src_dir, chapter_path)
