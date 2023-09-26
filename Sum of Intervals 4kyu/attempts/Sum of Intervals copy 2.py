def sum_of_intervals(intervals):
    min, max = 0, 0
    interval_list = []
    total = set()
    total.add((intervals[0][0], intervals[0][1]))
    total2 = [[intervals[0][0], intervals[0][1]]]

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    print(sorted_intervals)
    intervals = sorted_intervals

    for key, (start, end) in enumerate(intervals):
        print('key', key, start, end)
        total3 = total.copy()
        print('total 3 init', total3)
        for y in total3:
            print('start, end, y', start, end, y[0], y[1])
            if start in range(y[0]-1, y[1]+1) or end in range(y[0]-1, y[1]+1):
                min = y[0] if y[0] < start else start
                max = y[1] if y[1] > end else end
                print('min max', min, max)
                total.remove((y[0], y[1]))
                total.add((min, max))
                print('true', total)
            else:
                print('else', total, '+', start, end)
                total.add((start, end))
        print('total', total)

    return interval_list


if __name__=='__main__':
    x = [
        [1, 4],
        [7, 10],
        [3, 5],
    ]
    print(sum_of_intervals(x))
