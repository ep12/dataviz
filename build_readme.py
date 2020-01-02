import re
from urllib.parse import quote

RAW, CONVERT = 1, 2


def latex2url(latex_src: str, inline: bool):
    url = 'https://latex.codecogs.com/svg.latex?'
    if inline:
        url += '\\inline%20' * inline
    url += quote(latex_src)
    return f'![{latex_src}]({url})'


if __name__ == '__main__':
    with open('README.src.md') as f:
        raw = f.read()
    segments = []
    pos = 0
    for m in re.finditer(r'([\$]{1,2})([^\$].*?)\1', raw, re.DOTALL):
        span = m.span()
        segments.append((pos, span[0], RAW))
        segments.append((*span, CONVERT))
        pos = span[1]
    segments.append((pos, None, RAW))
    # print(segments)
    with open('README.md', 'w') as g:
        for start, end, mode in segments:
            if mode == RAW:
                g.write(raw[start:end])
                continue
            # mode == CONVERT
            part = raw[start:end]
            latex = part.strip('$').replace('\n', '')
            g.write(latex2url(latex, part[1] != '$'))
