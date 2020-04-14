import re


def get_unmatch_pos(code, start):
    """从code[start]开始向前搜索，返回第一个不匹配的左括号的位置"""
    left = 0
    for idx in range(start, -1, -1):
        chr = code[idx]
        if chr == ')':
            left -= 1
        elif chr == '(':
            left += 1
        # print('left:', left)
        if left == 1:
            return idx

    return -1


def get_linebreak_pos(code, start):
    """从code[start]开始向前搜索，返回第一个换行符的位置"""
    for idx in range(start, -1, -1):
        chr = code[idx]
        if chr == '\n':
            return idx

    return -1


def get_blank_pos(code, start):
    """从code[start]开始向前搜索，返回第一个空白的位置"""
    for idx in range(start, -1, -1):
        if code[abs(idx - 3):idx + 1] == ' ' * 4 or code[idx] == '\n':
            return idx

    return -1


def migrate_code(code):
    """将代码文本转换为PyWebIO中的调用"""

    re_render = re.compile(r"""(\.render\(["'].+?\.html["']\))""")
    pos = re_render.search(code)
    assert pos and len(pos.groups()) == 1, 'unknown code format'
    e = get_unmatch_pos(code, pos.start(1))
    if e == -1 and code[e - 1] != ' ':  # 单独调用chart.render("xxx.html")
        # code = re.sub(r"""(    |\n)(.+?)\.render\(["'].+?\.html["']\)""", ".render_notebook())", code)

        s = get_blank_pos(code, pos.start(1))
        assert s != -1, 'get_blank_pos()匹配错误'

        code = list(code)
        code[s + 1:s + 1] = 'put_html('
        code = ''.join(code)

        code = re.sub(re_render, ".render_notebook())\n", code)
    else:
        assert e != -1, '括号匹配错误'

        s = get_linebreak_pos(code, e)
        assert s != -1, '换行匹配错误'

        code = list(code)
        code[s:e] = '\nc = '
        code = ''.join(code)

        code = re.sub(re_render, "", code)
        code += '\nc.width = "100%"\nput_html(c.render_notebook())\n'

    code = "from pywebio.output import put_html\n" + code
    # code = re.sub(r"""open\(["'](.+?)["']""", r'open("%s/\g<1>"%workdir', code)
    return code
