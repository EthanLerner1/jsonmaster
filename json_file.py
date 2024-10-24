import json

from typing import TextIO

from pydantic import BaseModel
from json_namespace import JsonNamespace
from types import JsonValue


class JsonFile:
    def __init__(self, file_path: str, mode: str, immediate_flush: bool = False) -> None:
        self.__file_path: str = file_path
        self.__mode: str = mode
        self.__immediate_flush: bool = immediate_flush

    def __enter__(self) -> 'JsonFile':
        self.__file_fd: TextIO = open(self.__file_path, self.__mode)
        self.__data: dict = json.load(self.__file_fd)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            self.flush()
        finally:
            self.__file_fd.close()

    def __setitem__(self, key: str, value: JsonValue) -> None:
        self.__data.__setitem__(key, value)

        if self.__immediate_flush:
            self.flush()

    def __getitem__(self, key: str) -> None:
        self.__data.__getitem__(key)

    def __copy__(self) -> None:
        raise Exception("JsonFile cant be copied")

    def flush(self) -> None:
        START_OF_FILE: int = 0
        self.__file_fd.seek(START_OF_FILE)

        self.__file_fd.write(json.dumps(self.__data))

    def namespace(self) -> JsonNamespace:
        """
        This function returns a class which can be used to access the json data using .key instead of [key]
        :return: JsonNamespace
        """
        return JsonNamespace(self.__data)

    def dataclass(self, dataclass_type: BaseModel) -> BaseModel:
        return dataclass_type.parse_obj(self.__data)

