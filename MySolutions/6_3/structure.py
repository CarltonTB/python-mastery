import sys
import inspect


class Structure:
    _fields: tuple[str, ...]

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters.keys())

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

