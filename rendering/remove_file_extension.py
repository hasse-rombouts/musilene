import re


def remove_file_extensions(content: str):
    content = re.sub(r'href="index.html"', r'href="./"', content)
    return re.sub(r'href="([^"]+).html"', r'href="\1"', content)
