from validate import Integer, validated, enforce
from logcall import logformat, logged


@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    """
    Adds two numbers.
    """
    return x + y


@validated
@logged
def pow(x: Integer, y: Integer) -> Integer:
    """
    Raises a number to a power.
    """
    return x ** y


@validated
@logged
def sub(x: Integer, y: Integer) -> Integer:
    """
    Subtracts two numbers.
    """
    return x - y


@logformat(fmt='{fn.__code__.co_filename}:{fn.__name__}')
def mul(x, y):
    """
    Multiplies two numbers.
    """
    return x * y


class Spam:
    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
    def class_method(cls):
        pass

    @staticmethod
    @logged
    def static_method():
        pass

    @property
    @logged
    def property_method(self):
        pass

