from abc import ABC, abstractmethod



class TableFormatter(ABC):

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


from .formats import TextTableFormatter
from .formats import CSVTableFormatter
from .formats import HTMLTableFormatter

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin():
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def create_formatter(formatter_type, column_formats=['"%s"', '%d', '%0.2f'], upper_headers=False):
    mixins = [ColumnFormatMixin]
    if upper_headers:
        mixins += [UpperHeadersMixin]

    if formatter_type == 'text':
        class ComposedFormatter(*mixins, TextTableFormatter):
            formats = column_formats
            pass
    elif formatter_type == 'csv':
        class ComposedFormatter(*mixins, CSVTableFormatter):
            formats = column_formats
            pass
    elif formatter_type == 'html':
        class ComposedFormatter(*mixins, HTMLTableFormatter):
            formats = column_formats
            pass
    else:
        raise TypeError('invalid formatter type')

    return ComposedFormatter()



import sys

class RedirectStdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout

