def sum_of_intervals(intervals):
    min, max = 0, 0
    class ContinueI(Exception):
        pass
    continue_i = ContinueI()

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    print(sorted_intervals)
    intervals = sorted_intervals

    for i, x in enumerate(intervals):
        print('x', x)
        intervals2 = intervals.copy()
        intervals2.pop(i)
        try:
            for n, y in enumerate(intervals2):
                print('y, x', y, x)
                if x[0] <= y[0] <= x[1] or x[0] >= y[1] >= x[1]:
                    min = y[0] if y[0] < x[0] else x[0]
                    max = y[1] if y[1] > x[1] else x[1]
                    print('ints', intervals, intervals2)
                    intervals.remove([y[0], y[1]])
                    if [x[0], x[1]] in intervals:
                        intervals.remove([x[0], x[1]])
                    if [min, max] in intervals:
                        intervals.remove([min, max])
                    intervals.append([min, max])
                    print('add', [min, max])
                    print('remove y', y, intervals)
                    raise continue_i
                else:
                    if [x[0], x[1]] not in intervals:
                        intervals.append([x[0], x[1]])
        except ContinueI:
            continue

    sum_intervals = (sum(list(map(lambda x: x[1] - x[0], intervals))))

    return intervals, sum_intervals


if __name__=='__main__':
    x = [
        [1, 4],
        [7, 10],
        [3, 5],
        [0, 9]
    ]
    x = [
        [1, 5],
        [7, 10],
        [1, 5],
    ]
    x = [[1, 5],
        [10, 20],
        [1, 6],
        [16, 19],
        [5, 11]]
    
    print(sum_of_intervals(x))
