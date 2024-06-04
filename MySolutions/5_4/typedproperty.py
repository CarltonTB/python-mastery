def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value

class String:
    def __set_name__(self, cls, name):
        setattr(cls, name, typedproperty(name, str))

class Integer:
    def __set_name__(self, cls, name):
        setattr(cls, name, typedproperty(name, int))

class Float:
    def __set_name__(self, cls, name):
        setattr(cls, name, typedproperty(name, float))

