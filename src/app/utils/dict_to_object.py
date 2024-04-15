class DictToObject:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, self._convert(value))

    def _convert(self, value):
        if isinstance(value, dict):
            return DictToObject(value)
        elif isinstance(value, list):
            return [self._convert(item) for item in value]
        else:
            return value
