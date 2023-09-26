def sum_of_intervals(intervals):
    minn, maxn = 0, 0
    total = set()
    total.add((intervals[0][0], intervals[0][1]))

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    print(sorted_intervals)
    intervals = sorted_intervals

    for start, end in intervals:
        total_copy = total.copy()
        for y in total_copy:
            print('compare', start, end, y)
            print(start in range(y[0], y[1]+1))
            if start in range(y[0], y[1]+1) or end in range(y[0], y[1]+1):
                minn = y[0] if y[0] < start else start
                maxn = y[1] if y[1] > end else end
                total.remove((y[0], y[1]))
                total.add((minn, maxn))
                print('total new', total)
            else:
                total.add((start, end))
                print('total old', total)

    s = sum(list(map(lambda x: x[1] - x[0], total)))
    print('total', total, s)
    print(list(range(-5, -1)))
    return total


if __name__=='__main__':
    x = [
        [1, 4],
        [7, 10],
        [3, 5],
    ]
    x = [
        [1, 5],
        [7, 10],
        [1, 5],
    ]
    # x = [[1, 5],
    #     [10, 20],
    #     [1, 6],
    #     [16, 19],
    #     [5, 11]]

    # 1793 should equal 493
    # -227 -211, -15 462 = 493
    x = [(-387, -159), (-368, 336), (-341, 416), (-49, 468), (-26, 488), (37, 290), (84, 430), (92, 293), (253, 414), (266, 293), (324, 426), (378, 434), (418, 430), (481, 489)]
    x = [(-454, 446), (25, 206), (80, 243), (115, 193), (142, 342), (181, 392), (289, 316), (373, 452), (417, 461), (470, 495)]
    x = [(-227, -211), (-15, 428), (-11, 310), (90, 392), (134, 173), (232, 462), (258, 324), (355, 421), (389, 432)]

    print(sum_of_intervals(x))
