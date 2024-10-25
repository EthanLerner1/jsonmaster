from jsonmaster.jsonfile.json_file import JsonFile


def open_json(file_path: str) -> JsonFile:
    """
    Simple json file creation.
    For more options create a JsonFile yourself
    :param file_path: filepath of the json file
    :return: JsonFile instance
    """
    return JsonFile(file_path=file_path)