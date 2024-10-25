from jsonmaster.jsonfile.json_file import JsonFile


def open_json(file_path: str) -> JsonFile:
    return JsonFile(file_path=file_path)
