class Structure:
    _fields: tuple[str, ...]

    @classmethod
    def create_init(cls):
        args = ','.join(cls._fields)
        inits = '\n'.join([
            f'  self.{field} = {field}'
            for field in cls._fields
        ])
        init_str = f"def __init__(self, {args}):\n{inits}"
        locs = {}
        exec(init_str, locs)
        cls.__init__ =  locs['__init__']

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

