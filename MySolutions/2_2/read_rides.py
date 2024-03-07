# readrides.py

import csv
from collections import Counter, defaultdict

def read_rides(filename):
    route_set = set()
    rides_by_route = Counter()
    rides_by_date_and_route = defaultdict(Counter)
    rides_by_year_and_route = defaultdict(Counter)
    f = open(filename)
    rows = csv.reader(f)
    headings = next(rows)     # Skip headers
    for row in rows:
        route = row[0]
        date = row[1]
        daytype = row[2]
        rides = int(row[3])
        route_set.add(route)
        rides_by_route[route] += rides
        rides_by_date_and_route[date][route] += rides
        year = date.split('/')[2]
        rides_by_year_and_route[year][route] += rides

    f.close()
    return route_set, rides_by_route, rides_by_date_and_route, rides_by_year_and_route


if __name__ == '__main__':
    filename = '../../Data/ctabus.csv'
    routes, rides_by_route, rides_by_date_and_route, rides_by_year_and_route = read_rides(filename)

    print('Total routes:', len(routes))
    print('Riders on bus 22 on Feb 2nd, 2011:', rides_by_date_and_route['02/02/2011']['22'])
    print('Total rides on each route:', rides_by_route)

    ridership_increases = []
    for route in routes:
        increase = rides_by_year_and_route['2011'][route] - rides_by_year_and_route['2001'][route]
        ridership_increases.append((route, increase))

    ridership_increases.sort(reverse=True, key=lambda x: x[1])
    print('Ridership increases from 2001 to 2011:', ridership_increases)

