from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()


if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter(
            formatter_type='text',
            column_formats=[
                '%s',
                '%0.2f',
                '%0.2f',
            ]
    )
    lines = follow('../../Data/stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negatives = (r for r in records if r.change < 0)

    print_table(negatives, ['name', 'price', 'change'], formatter)

