import csv
from typing import List, Dict, TypeVar, Any

T = TypeVar('T')

def convert_csv(lines, row_fn, headers=None) -> List[Any]:
    rows = csv.reader(lines)
    headers = headers or next(rows)
    return list(map(lambda row: row_fn(row, headers), rows))


def csv_as_dicts(lines: List[List[str]], types: List[T], headers=None) -> List[Dict]:
    row_fn = lambda row, headers: {name: fn(v) for name, fn, v in zip(headers, types, row)}
    return convert_csv(lines, row_fn, headers)
    

def read_csv_as_dicts(filename: str, types: List[T]) -> List[Dict]:
    with open(filename) as file:
        return csv_as_dicts(file, types)


def csv_as_instances(lines: List[List[str]], cls: T, headers=None) -> List[T]:
    return convert_csv(lines, cls.from_row, headers)


def read_csv_as_instances(filename: str, cls: T) -> List[T]:
    with open(filename) as file:
        return csv_as_instances(file, cls)

