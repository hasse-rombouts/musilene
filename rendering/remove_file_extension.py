import re


def remove_file_extensions(content: str):
    return re.sub(r'href="([^"]+).html"', r'href="\1"', content)
