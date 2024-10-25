import json
import os.path

from typing import TextIO, Type

from pydantic import BaseModel
from jsonmaster.json_namespace import JsonNamespace
from jsonmaster.types import JsonValueType, _T


class JsonFile:
    def __init__(self, file_path: str, immediate_flush: bool = False, sort_keys: bool = False, prettify: bool = False) -> None:
        self.__file_path: str = file_path
        self.__immediate_flush: bool = immediate_flush
        self.__sort_keys: bool = sort_keys
        self.__prettify: bool = prettify
        self.__file_fd: TextIO = open(self.__file_path, "r+" if os.path.exists(file_path) else "w+")
        self.__data: dict = self.__read_dict()

    def __enter__(self) -> 'JsonFile':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            self.flush()
        finally:
            self.__file_fd.close()

    def __setitem__(self, key: str, value: JsonValueType) -> None:
        self.__data[key] = value

        if self.__immediate_flush:
            self.flush()

    def __getitem__(self, key: str) -> None:
        return self.__data[key]

    def __copy__(self) -> None:
        raise Exception("JsonFile cant be copied")

    def dict(self) -> dict:
        return self.__data

    def flush(self) -> None:
        self.__seek_start()
        self.__file_fd.write(json.dumps(self.__data, sort_keys=self.__sort_keys, indent=4 if self.__prettify else 0))

    def namespace(self) -> JsonNamespace:
        """
        This function returns a class which can be used to access the json data using .key instead of [key]
        :return: JsonNamespace
        """
        return JsonNamespace(self.__data)

    def dataclass(self, basemodel_type: Type[_T]) -> _T:
        if not issubclass(basemodel_type, BaseModel):
            raise Exception("This feature is only supported for classes which inherit from Pydantic BaseModel")

        return basemodel_type.parse_obj(self.__data)

    def __read_dict(self) -> dict:
        file_content: str = self.__file_fd.read()
        if not file_content:
            return {}

        return json.loads(file_content)

    def __seek_start(self) -> None:
        START_OF_FILE: int = 0
        self.__file_fd.seek(START_OF_FILE)
