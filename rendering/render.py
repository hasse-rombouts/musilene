import re
from typing import Any, Dict


def render_words(text: str, data: Dict[str, Any]) -> str:
    word_pattern = r"{{\s*(?P<key>[\w\.]+)\s*}}"

    def replace(match, data):
        key = match.group("key")
        nested_keys = key.split(".")
        for nested_key in nested_keys:
            if nested_key not in data:
                raise Exception(
                    f"Is seems like you forgot to add the collection data for the key `{nested_key}`"
                )
            data = data[nested_key]
        return data

    return re.sub(word_pattern, lambda match: replace(match, data), text)


def format_file(file_content: str, data: Dict[str, Any]) -> str:
    for_pattern = r"{{\s*for\s+(?P<key>[\w\.]+)\s+in\s+(?P<collection>[\w\.]+)\s*}}\n*(?P<content>[\s\S]*?)\n*{{\s*endfor\s*}}\n*"

    def replace(match, data):
        collection_key = match.group("collection")
        nested_keys = collection_key.split(".")
        collection = data
        for nested_key in nested_keys:
            if nested_key not in collection:
                raise Exception(
                    f"Is seems like you forgot to add the collection data for the key `{collection_key}`"
                )
            collection = collection[nested_key]
        if not isinstance(collection, list):
            raise Exception(
                f"The key `{nested_key}` is not a list but is used in a for loop"
            )
        return "\n".join(
            [
                render_words(match.group("content"), {match.group("key"): item})
                for item in collection
            ]
        )

    formatted = re.sub(for_pattern, lambda match: replace(match, data), file_content)
    return render_words(formatted, data)
