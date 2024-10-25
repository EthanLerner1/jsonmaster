from typing import List, Union, TypeVar

from pydantic import BaseModel

JsonBasicValueType = Union[int, str]
JsonValueType = Union[int, str, List[JsonBasicValueType]]

_T = TypeVar('_T', bound=BaseModel)

