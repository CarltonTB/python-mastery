import os
import time


def follow(filepath: str):
    f = open(filepath)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        else:
            yield line


if __name__ == '__main__':
    for line in follow('../../Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('""')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))

