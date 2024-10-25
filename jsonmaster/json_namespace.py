class JsonNamespace:
    def __init__(self, data_dict: dict) -> None:
        for key, value in data_dict.items():
            if type(value) is dict:
                setattr(self, key, JsonNamespace(value))
            else:
                setattr(self, key, value)

    def __getattr__(self, key):
        try:
            return self.__dict__[key]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")