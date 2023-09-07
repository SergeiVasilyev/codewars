def make_readable(seconds):
    if seconds < 359999:
        remainder_minus_hours = seconds % 3600
        m = remainder_minus_hours // 60
        s = remainder_minus_hours % 60
        h = seconds // 3600
    else:
        return '99:59:59'
    return f'{h:02d}:{m:02d}:{s:02d}'




if __name__=='__main__':
    print(make_readable(0), "-> 00:00:00")
    print(make_readable(5), "-> 00:00:05")
    print(make_readable(180), "-> 00:03:00")
    print(make_readable(86399), "-> 23:59:59")
    print(make_readable(86395), "-> 23:59:55")
    print(make_readable(359999), "-> 99:59:59")
    print(make_readable(360000), "-> 99:59:59")
