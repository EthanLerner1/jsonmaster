# JSONMaster

**JSONMaster** is a Python package designed to provide a collection of utilities for working with JSON data.
Whatever you are doing with jsons, **JSONMaster**,aims to simplify your workflow and enhance your productivity.

## Features

- **Easy Parsing**: Effortlessly parse JSON strings into Python objects.
- **Transformation**: Transform JSON structures with intuitive functions to namespaces or dataclasses.
- **File I/O**: Simplify reading from and writing to JSON files.

## Installation

You can install JSONMaster via pip:

```bash
pip install jsonmaster
```

## Usage

### Reading a json file

Read a json from a file path
```python
from jsonmaster import open_json, JsonFile

# easy option
with open_json("jsonfile.json") as jf:
    print(jf.dict())

# configurable option
with JsonFile(file_path="jsonfile.json", sort_keys=True, immediate_flush=True, prettify=True) as jf:
    print(jf.dict())
```


### Using regular json package

All regular [json package](https://docs.python.org/3/library/json.html) capabilities are imported inside jsonmaster

```python
import jsonmaster

data: str = '{"name": "Alice", "age": 30}'

d: dict = jsonmaster.loads(data)

print(jsonmaster.dumps(d))

# ...
```

### Accessing json as a namespace

Use your jsons as an actual python class
```python
from jsonmaster import open_json, JsonNamespace

# jsonfile.json contains {"key": "value"}
with open_json("jsonfile.json") as jf:
    namespace: JsonNamespace = jf.namespace()
    
    # access the key 
    print(namespace.key)
    
    # set will not affect the original file

```

### File I/O

Read and write JSON files easily:

```python
from jsonmaster import open_json

# jsonfile.json contains {"key": "value"}
with open_json("jsonfile.json") as jf:
    # Adding a new key to the json file
    jf["new_key"] = "new_value"
    
    # Accessing an existing key in the json file
    print(jf["old_key"])
    print(jf["new_key"])

```


### Dataclasses

Load your json file into your **pydantic** BaseModel easily

```python
from jsonmaster import open_json
from pydantic import BaseModel


class MyModel(BaseModel):
    my_model_str_key: str
    my_model_int_key: int


with open_json('jsonfile.json') as jf:
    m: MyModel = jf.dataclass(MyModel)
    print(m.my_model_str_key)
```

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Author

Created by [Ethan Lerner](https://github.com/EthanLerner1).

