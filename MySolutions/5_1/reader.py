import csv
from typing import List, Dict, TypeVar

T = TypeVar('T')

def csv_as_dicts(lines: List[List[str]], types: List[T], headers=None) -> List[Dict]:
    rows = csv.reader(lines)
    headers = headers or next(rows)
    records = []
    for row in rows:
        record = {name: fn(v) for name, fn, v in zip(headers, types, row)}
        records.append(record)

    return records
    

def read_csv_as_dicts(filename: str, types: List[T]) -> List[Dict]:
    with open(filename) as file:
        return csv_as_dicts(file, types)


def csv_as_instances(lines: List[List[str]], cls: T, headers=None) -> List[T]:
    rows = csv.reader(lines)
    headers = headers or next(rows)
    records = []
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    
    return records


def read_csv_as_instances(filename: str, cls: T) -> List[T]:
    with open(filename) as file:
        return csv_as_instances(file, cls)

