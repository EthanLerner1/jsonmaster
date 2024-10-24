from json_file import JsonFile


def read_json(file_path: str) -> JsonFile:
    return JsonFile(file_path=file_path, mode='r')


def read_write_json_file(file_path: str) -> JsonFile:
    return JsonFile(file_path=file_path, mode='rw')
