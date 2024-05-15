from abc import ABC, abstractmethod

class TableFormatter(ABC):

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(v) for v in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        result = ''
        for header in headers:
            result += f'<th>{header}</th>'
        print('<tr>' + result + '</tr>')

    def row(self, rowdata):
        result = ''
        for data in rowdata:
            result += f'<td>{data}</td>'
        print('<tr>' + result + '</tr>')


def create_formatter(formatter_type):
    if formatter_type == 'text':
        return TextTableFormatter()
    elif formatter_type == 'csv':
        return CSVTableFormatter()
    elif formatter_type == 'html':
        return HTMLTableFormatter()
    else:
        raise TypeError('invalid formatter type')


def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

import sys

class RedirectStdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout

