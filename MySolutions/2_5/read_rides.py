# readrides.py

import csv
from collections import namedtuple, abc

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

class RideData(abc.Sequence):
    def __init__(self, routes=[], dates=[], daytypes=[], numrides=[]):
        self.routes = routes
        self.dates = dates
        self.daytypes = daytypes
        self.numrides = numrides

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, int):
            return { 'route': self.routes[index],
                     'date': self.dates[index],
                     'daytype': self.daytypes[index],
                     'rides': self.numrides[index] }
        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            return RideData(self.routes[start:stop:step], self.dates[start:stop:step],
                            self.daytypes[start:stop:step], self.numrides[start:stop:step]
                            )

    def __setitem__(self, key, val):
        self.routes[key] = val['routes']
        self.dates[key] = val['date']
        self.daytypes[key] = val['daytype']
        self.rides[key] = val['rides']

    def __delitem__(self, key):
        del self.routes[key]
        del self.dates[key]
        del self.daytypes[key]
        del self.rides[key]

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

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
    records = RideData()
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

def read_rides_as_columns(filename):
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))

        return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
                        

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

    tracemalloc.stop()
    tracemalloc.start()
    rows = read_rides_as_columns(filename)
    print('Memory use with columns: Current %d, Peak %d' % tracemalloc.get_traced_memory())

