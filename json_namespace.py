class JsonNamespace:
    def __init__(self, data_dict: dict) -> None:
        for key, value in data_dict.items():
            setattr(self, key, value)
