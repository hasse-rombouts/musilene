import json
import os
import glob
import shutil
from typing import Dict

from render import format_file

def index_files():
    folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../build'))
    shutil.rmtree(folder_path)
    files = []
    src_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
    for dirpath, _, filenames in os.walk(src_folder):
        for filename in filenames:
            if not filename.endswith('.html'):
                src_path = os.path.join(dirpath, filename)
                dest_path =src_path.replace('/src/', '/build/')
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(src_path, dest_path)
            else: 
                files.append(os.path.join(dirpath, filename))
    return files

def process_file(filename: str, data: Dict):
    with open(filename, 'r') as f:
        content = f.read()
        result = format_file(content, data)
        
        build_file = filename.replace('/src/', '/build/')
        os.makedirs(os.path.dirname(build_file), exist_ok=True)
        with open(build_file, 'w') as f:
            f.write(result)

def get_data():
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '../content/data.json'))
    with open(filename, 'r') as f:
        return json.load(f)

def build():
    files = index_files()
    data = get_data()
    for file in files:
        process_file(file, data)

if __name__ == '__main__':
    build()