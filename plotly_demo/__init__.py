import re
from functools import partial
from os import path

from pywebio.input import *
from pywebio.output import *
from .inventory import all_demos

here = path.dirname(path.abspath(__file__))

demos_dir = path.join(here, 'demos')


def show_hide_code(btn, code='', after=''):
    remove('code')
    remove('remove-code-btn')

    if btn == '查看源码':
        put_code(code, 'python', after=after, anchor='code')
        put_buttons(['隐藏源码'], onclick=show_hide_code, anchor='remove-code-btn', after='code')


async def exec_md(md):
    parts = re.split(r"(```[\s\S]*?```)", md)
    for idx, part in enumerate(parts):
        if part.startswith('```put_html'):
            put_html(part[len("```put_html"):-3].strip())
        elif part.startswith('```python') and 'pywebio' in part:
            code = part[len("```python"):-3].strip()
            anchor = 'show-code-%s' % idx
            put_buttons(['查看源码'], onclick=partial(show_hide_code, code=code, after=anchor), anchor=anchor)
        else:
            put_markdown(part)


async def show_demo(name, chapter):
    clear_after('demo-start')
    set_anchor('demo-start')

    title = all_demos.get(chapter, {}).get(name, name)
    put_markdown("### %s" % title)

    chapter_dir = chapter.replace(" ", "-").lower()
    md_file = path.join(demos_dir, chapter_dir, name + '.md')
    if not path.isfile(md_file):
        return
    md = open(md_file).read()
    await exec_md(md)


async def show_chapter(chapter):
    clear_after('chapter-start')
    set_anchor('chapter-start')

    put_markdown("### %s" % chapter)
    demos = all_demos.get(chapter, {})

    chapter_dir = chapter.replace(" ", "-").lower()
    buttons = [
        (v, k) for k, v in demos.items()
        if path.isfile(path.join(demos_dir, chapter_dir, k + '.md'))
    ]
    put_buttons(buttons=buttons,
                onclick=partial(show_demo, chapter=chapter))

    put_markdown('-----------')


async def plotly_demo():
    set_auto_scroll_bottom(False)
    set_title("Plotly Demo")

    put_markdown(r"""## Plotly

    [plotly.py](https://github.com/plotly/plotly.py) 是一个非常流行的Python数据可视化库，可以生成高质量的交互式图表

    PyWebIO 支持输出使用 plotly 库创建的图表。使用方式为在PyWebIO会话中调用 
    ```python
    # fig 为 plotly 的图表实例
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    pywebio.output.put_html(html)
    ``` 
    具体可以参考下面demo中的源码。

    ## Demos List
    
    以下示例修改自 [plotly官方文档](https://plotly.com/python/)
    
    ### Category
    """, strip_indent=4)

    put_buttons(list(all_demos.keys()), onclick=show_chapter)

    await actions(buttons=['Quit'])
