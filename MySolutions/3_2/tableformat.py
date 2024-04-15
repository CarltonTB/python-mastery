def print_table(objs, cols):
    col_count = len(cols)
    format_str = '%10s ' * col_count
    format_str.strip()
    print(format_str % tuple(cols))
    break_str = ('-'*10 + ' ') * col_count
    break_str.strip()
    print(break_str)
    for obj in objs:
        vals = [getattr(obj, col) for col in cols]
        print(format_str % tuple(vals))

