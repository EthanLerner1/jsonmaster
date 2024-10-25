import json
import os

import pytest

from jsonmaster import JsonFile


@pytest.fixture
def temp_json_file():
    # Create a temporary JSON file for testing
    file_path = 'test.json'
    with open(file_path, 'w') as f:
        json.dump({"key": "value"}, f)
    yield file_path
    # Remove the temporary JSON file after tests
    os.remove(file_path)


def test_read_json(temp_json_file):
    with JsonFile(file_path=temp_json_file) as jf:
        data = jf.dict()
        assert data == {"key": "value"}


def test_write_json(temp_json_file):
    with JsonFile(file_path=temp_json_file) as jf:
        jf["new_key"] = "new_value"
        jf.flush()

    with open(temp_json_file, 'r') as f:
        data = json.load(f)
        assert data == {"key": "value", "new_key": "new_value"}


def test_flush_immediate(temp_json_file):
    with JsonFile(file_path=temp_json_file, immediate_flush=True) as jf:
        jf["another_key"] = "another_value"

    with open(temp_json_file, 'r') as f:
        data = json.load(f)
        assert data == {"key": "value", "another_key": "another_value"}


def test_namespace_access(temp_json_file):
    with JsonFile(file_path=temp_json_file) as jf:
        namespace = jf.namespace()
        assert namespace.key == "value"
