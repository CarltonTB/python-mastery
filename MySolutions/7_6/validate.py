import inspect
from functools import wraps

class Validator:

    validators = {}
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls

    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class Typed(Validator):
    expect_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)


def validated(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        errors = ''
        for k, v in sig.bind(*args, **kwargs).arguments.items():
            try:
                annotated_type = fn.__annotations__[k]
            except KeyError:
                continue

            try:
                annotated_type.check(v)
            except Exception as e:
                errors += f'{k}: {str(e)}\n'

        if errors:
            raise TypeError(f'Bad arguments:\n{errors}')

        result = fn(*args, **kwargs)

        if hasattr(sig.return_annotation, 'check'):
            try:
                sig.return_annotation.check(result)
            except Exception as e:
                raise TypeError(f'Bad return: {str(e)}')

        return result 

    return wrapper


def enforce(**type_annotations):
    return_type = type_annotations.pop('return_', None)

    def decorate(fn):
        sig = inspect.signature(fn)
        @wraps(fn)
        def wrapper(*args, **kwargs):
            fn_arguments = sig.bind(*args, **kwargs).arguments 
            errors = ''
            for arg_name, _type in type_annotations.items():
                try:
                    value = fn_arguments[arg_name]
                except KeyError:
                    continue

                try:
                    _type.check(value)
                except Exception as e:
                    errors += f'{arg_name}: {str(e)}\n'

            if errors:
                raise TypeError(f'Bad arguments:\n{errors}')

            result = fn(*args, **kwargs)

            if return_type:
                try:
                    return_type.check(result)
                except Exception as e:
                    raise TypeError(f'Bad return: {str(e)}')

            return result 
        return wrapper
    return decorate


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


class NonEmptyString(String, NonEmpty):
    pass

