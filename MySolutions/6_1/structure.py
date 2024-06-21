class Structure:
    _fields: tuple[str]

    def __init__(self, *args, **kwargs):
        expected_arg_count = len(self._fields)
        
        if (len(args) + len(kwargs.items())) != expected_arg_count:
            raise TypeError(f'Expected {expected_arg_count} arguments')

        for i, arg in enumerate(args):
            setattr(self, self._fields[i], arg)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __setattr__(self, field, val):
        if field not in self._fields and not field.startswith('_'):
            raise AttributeError(f'No attribute {field}')

        super().__setattr__(field, val)


    def __repr__(self):
        properties = []
        for field in self._fields:
            val = getattr(self, field)
            if isinstance(val, str):
                properties.append(f"'{val}'")
            else:
                properties.append(str(val))
        return f'{type(self).__name__}({", ".join(properties)})'

