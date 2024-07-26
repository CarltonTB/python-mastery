import sys
from abc import ABC, abstractmethod


class TableFormatter(ABC):
    _formats = dict()

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls


    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin():
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def create_formatter(formatter_type, column_formats=['"%s"', '%d', '%0.2f'], upper_headers=False):
    if formatter_type not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{formatter_type}')

    formatter_cls = TableFormatter._formats.get(formatter_type)

    if not formatter_cls:
        raise RuntimeError(f'Unknown format: {formatter_type}')

    mixins = [ColumnFormatMixin]
    if upper_headers:
        mixins += [UpperHeadersMixin]

    class ComposedFormatter(*mixins, formatter_cls):
        formats = column_formats

    return ComposedFormatter()



class RedirectStdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout

