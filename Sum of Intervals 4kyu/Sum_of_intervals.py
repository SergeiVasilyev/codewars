def sum_of_intervals(intervals):
    minn, maxn = 0, 0
    total = []
    total.append([intervals[0][0], intervals[0][1]])

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    intervals = sorted_intervals

    for start, end in intervals:
        total_copy = total.copy()
        for y in total_copy:
            if y[0] <= start <= y[1] or y[0] >= end >= y[1]:
                minn = y[0] if y[0] < start else start
                maxn = y[1] if y[1] > end else end
                total.remove([y[0], y[1]])
                if [start, end] in total:
                    total.remove([start, end])
                if [minn, maxn] not in total:
                    total.append([minn, maxn])
            else:
                if [start, end] not in total:
                    total.append([start, end])

    s = sum(list(map(lambda x: x[1] - x[0], total)))
    return total, s


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
    x = [[1, 5],
        [10, 20],
        [1, 6],
        [16, 19],
        [5, 11]]

    # 876
    x = [(-387, -159), (-368, 336), (-341, 416), (-49, 468), (-26, 488), (37, 290), (84, 430), (92, 293), (253, 414), (266, 293), (324, 426), (378, 434), (418, 430), (481, 489)]
    # 940
    # x = [(-454, 446), (25, 206), (80, 243), (115, 193), (142, 342), (181, 392), (289, 316), (373, 452), (417, 461), (470, 495)]
    # 493
    # x = [(-227, -211), (-15, 428), (-11, 310), (90, 392), (134, 173), (232, 462), (258, 324), (355, 421), (389, 432)]
    # 986
    # x = [(-493, 17), (-438, 385), (-159, -74), (-114, -23), (-73, 289), (-24, 465), (-22, 283), (69, 193), (111, 434), (159, 281), (185, 205), (192, 392), (196, 255), (203, 468), (249, 384), (261, 421), (300, 493), (359, 493)]
    # 887
    # x = [(-485, 123), (-414, -200), (-372, 58), (-371, -98), (-330, 87), (-231, 8), (-22, 184), (42, 236), (134, 216), (320, 444), (368, 486), (403, 485), (435, 463)]
    # 916
    # x = [(-444, 144), (-320, -13), (-224, -133), (-146, -116), (-92, 387), (54, 339), (108, 472), (204, 420), (226, 316), (233, 408), (256, 410)]


    res = sum_of_intervals(x)
    print(res)
    print('All non-overlapping intervals', res[0], 'Sum of all intervals', res[1])
