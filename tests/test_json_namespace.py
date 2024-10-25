import pytest

from jsonmaster.json_namespace import JsonNamespace


@pytest.fixture
def json_namespace():
    test_data = {"key": "value", "nested": {"inner_key": "inner_value"}}
    return JsonNamespace(test_data)


def test_attribute_access(json_namespace):
    assert json_namespace.key == "value"


def test_nested_attribute_access(json_namespace):
    assert json_namespace.nested.inner_key == "inner_value"


def test_invalid_attribute_access(json_namespace):
    with pytest.raises(AttributeError):
        _ = json_namespace.non_existent_key
