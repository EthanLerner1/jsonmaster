from jsonmaster import recursive_update


def test_update_with_nested_dicts():
    base = {"a": 1, "b": {"c": 2}}
    overlay = {"b": {"d": 3}, "e": 4}
    expected = {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
    result = recursive_update(base, overlay)
    assert result == expected


def test_update_with_non_nested_dicts():
    base = {"a": 1, "b": 2}
    overlay = {"b": 3, "c": 4}
    expected = {"a": 1, "b": 3, "c": 4}
    result = recursive_update(base, overlay)
    assert result == expected


def test_update_with_conflicting_keys():
    base = {"a": 1}
    overlay = {"a": 2}
    expected = {"a": 2}
    result = recursive_update(base, overlay)
    assert result == expected
