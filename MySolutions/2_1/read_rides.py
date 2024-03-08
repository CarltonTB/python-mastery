# readrides.py

import csv
from collections import namedtuple


RowTuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

class RowSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = RowTuple(row[0], row[1], row[2], int(row[3]))
            records.append(record)

    return records

def read_rides_as_class(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)

    return records

def read_rides_as_class_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = RowSlots(row[0], row[1], row[2], int(row[3]))
            records.append(record)

    return records

def read_rides_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3]),
            }
            records.append(record)
        return records


if __name__ == '__main__':
    filename = '../../Data/ctabus.csv'
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples(filename)
    print('Memory use with tuples: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    tracemalloc.stop()
    tracemalloc.start()
    rows = read_rides_as_named_tuples(filename)
    print('Memory use with named tuples: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    tracemalloc.stop()
    tracemalloc.start()
    rows = read_rides_as_class(filename)
    print('Memory use with class: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    tracemalloc.stop()
    tracemalloc.start()
    rows = read_rides_as_class_slots(filename)
    print('Memory use with class slots: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    tracemalloc.stop()
    tracemalloc.start()
    rows = read_rides_as_dicts(filename)
    print('Memory use with dicts: Current %d, Peak %d' % tracemalloc.get_traced_memory())

