import re
from functools import partial
from os import path

from pywebio.output import *
from pywebio.session import info as session_info
from .inventory import all_demos

here = path.dirname(path.abspath(__file__))

demos_dir = path.join(here, 'demos')


def t(eng, chinese):
    """return English or Chinese text according to the user's browser language"""
    return chinese if 'zh' in session_info.user_language else eng


async def exec_md(md):
    parts = re.split(r"(```[\s\S]*?```)", md)
    for idx, part in enumerate(parts):
        if part.startswith('```put_html'):
            put_html(part[len("```put_html"):-3].strip())
        elif part.startswith('```python') and 'pywebio' in part:
            code = part[len("```python"):-3].strip()

            put_collapse(t('Show source code', '查看源码'), put_code(code, 'python'))
        else:
            put_markdown(part)


@use_scope('demo', clear=True)
async def show_demo(name, chapter):
    title = all_demos.get(chapter, {}).get(name, name)
    put_markdown("### %s" % title)
    scroll_to(position='top')
    with use_scope('loading'):
        put_text('Loading....')
        put_loading()

    chapter_dir = chapter.replace(" ", "-").lower()
    md_file = path.join(demos_dir, chapter_dir, name + '.md')
    if not path.isfile(md_file):
        return
    md = open(md_file).read()
    await exec_md(md)

    scroll_to(position='top')
    clear('loading')


@use_scope('chapter', clear=True)
async def show_chapter(chapter):
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
    """PyWebIO plotly Demo

    Demo of using plotly for data visualization in PyWebIO.
    在PyWebIO中使用 plotly 进行数据可视化示例
    """

    put_markdown(t(r"""## plotly

    [plotly.py](https://github.com/plotly/plotly.py) is an interactive, open-source, and browser-based graphing library for Python.

    In PyWebIO, you can use the following code to output the plotly chart instance:
    ```python
    # fig is plotly chart instance
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    pywebio.output.put_html(html)
    ``` 
    For details, please refer to the source code of the demo below.

    ## Demos List
    
    The following example is modified from the [official plotly document](https://plotly.com/python/)
    
    ### Category
    """, r"""## plotly

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
    """), strip_indent=4)

    put_buttons(list(all_demos.keys()), onclick=show_chapter)
