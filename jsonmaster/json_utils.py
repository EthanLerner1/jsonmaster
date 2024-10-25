def recursive_update(base_dict: dict, overlay_dict: dict) -> dict:
    """
        Recursively merge overlay into base.
        If keys in both dictionaries are dictionaries themselves, merge them recursively.
        Otherwise, the value from overlay_dict will overwrite the value in base_dict.

        Args:
        base_dict (dict): The first dictionary.
        overlay_dict (dict): The second dictionary.

        Returns:
        dict: A new dictionary containing the recursively merged contents.
        """
    merged_dict: dict = base_dict.copy()

    for key, value in overlay_dict.items():
        if key in merged_dict and isinstance(merged_dict[key], dict) and isinstance(value, dict):
            merged_dict[key] = recursive_update(merged_dict[key], value)
        else:
            merged_dict[key] = value

    return merged_dict
