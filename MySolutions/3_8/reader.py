from abc import ABC, abstractmethod
import csv
from collections import abc

class DataCollection(abc.Sequence):
    def __init__(self, headers, types, rows=None):
        self.types = types
        self.headers = headers
        rows = rows or [[] for i in range(len(self.headers))]
        for header, r in zip(self.headers, rows):
            setattr(self, header, r)

    def __len__(self):
        return len(getattr(self, self.headers[0]))

    def __getitem__(self, index):
        if isinstance(index, int):
            return { col: getattr(self, col)[index] for col in self.headers}
        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            return DataCollection(
                    self.headers,
                    [getattr(self, header)[start:stop:step] for header in self.headers],
                    self.types
                    )

    def __setitem__(self, index, val):
        for header, fn in zip(self.headers, self.types):
            setattr(self, header)[index] = fn(val[header]) 

    def __delitem__(self, key):
        for header in self.headers:
            del getattr(self, header)[key]

    def append(self, row):
        for header, value, fn in zip(self.headers, row, self.types):
            getattr(self, header).append(fn(value))


class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                records.append(self.make_record(headers, row))

        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass


class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { k: fn(v) for k, v, fn in zip(headers, row, self.types)}


class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)


def read_csv_as_dicts(path, types):
    return DictCSVParser(types).parse(path)

def read_csv_as_instances(path, cls):
    return InstanceCSVParser(cls).parse(path)

def read_csv_as_columns(path, types):
    f = open(path)
    rows = csv.reader(f)
    headers = next(rows)
    collection = DataCollection(headers, types)
    for row in rows:
        collection.append(row)

    return collection


if __name__ == "__main__":
    data = read_csv_as_columns('../../Data/ctabus.csv', [str, str, str, int])
    len(data)
    print(data)
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[:10])

