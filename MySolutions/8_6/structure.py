from validate import Validator, validated
from collections import ChainMap


class StructureMeta(type):

    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)


class Structure(metaclass=StructureMeta):
    _fields: tuple[str, ...]
    _types = tuple()

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)

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
        cls.__init__ = locs['__init__']

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

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)

    @classmethod
    def from_row(cls, row):
        rowdata = [fn(v) for fn, v in zip(cls._types, row)]
        return cls(*rowdata)


def validate_attributes(cls):
    validators = []
    types = []
    for name, v in vars(cls).items():
        if isinstance(v, Validator):
            validators.append(v)
            expected_type = getattr(v, 'expected_type')
            if expected_type:
                types.append(expected_type)
        elif callable(v) and v.__annotations__:
            setattr(cls, name, validated(v))

    cls._fields = tuple(v.name for v in validators)
    cls._types = tuple(types)
    
    if cls._fields:
        cls.create_init()

    return cls

