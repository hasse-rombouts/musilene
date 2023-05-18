import json
import os
import shutil
import sys
import time
from typing import Dict

from render import format_file
from copy_flyer import copy_flyer
from remove_file_extension import remove_file_extensions


def index_files():
    path_one_level_up = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    folder_path = os.path.join(path_one_level_up, "build")
    shutil.rmtree(folder_path, ignore_errors=True)
    files = []
    src_folder = os.path.join(path_one_level_up, "src")
    for dirpath, _, filenames in os.walk(src_folder):
        for filename in filenames:
            if not filename.endswith(".html"):
                src_path = os.path.join(dirpath, filename)
                dest_path = src_path.replace("\\src\\", "\\build\\").replace(
                    "/src/", "/build/"
                )
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(src_path, dest_path)
            else:
                files.append(os.path.join(dirpath, filename))
    return files


def process_file(filename: str, data: Dict, deploy):
    if os.path.isdir(filename):
        return
    if not filename.endswith(".html"):
        print("Copying file", filename)
        dest_path = filename.replace("\\src\\", "\\build\\").replace("/src/", "/build/")
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(filename, dest_path)
        return

    with open(filename, "r") as f:
        content = f.read()
        result = format_file(content, data)
        if deploy:
            result = remove_file_extensions(result)

        build_file = filename.replace("\\src\\", "\\build\\").replace(
            "/src/", "/build/"
        )
        os.makedirs(os.path.dirname(build_file), exist_ok=True)
        with open(build_file, "w") as f:
            f.write(result)


def get_data():
    filename = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "content", "data.json")
    )
    with open(filename, "r") as f:
        return json.load(f)


def build(deploy: bool):
    files = index_files()
    data = get_data()
    for file in files:
        process_file(file, data, deploy)
    copy_flyer()


if __name__ == "__main__":
    t0 = time.perf_counter()
    deploy = len(sys.argv) > 1 and sys.argv[1] == "deploy"
    build(deploy)
    t1 = time.perf_counter()
    print(f"Build completed in {t1-t0:0.4f} seconds")
