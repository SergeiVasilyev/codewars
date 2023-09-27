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
        total3 = sorted(total.copy()) # For proper operation, the set must be sorted 
        print('total 3 init', total3)
        for y in total3:
            print('start, end, y', start, end, y[0], y[1])
            if y[0] <= start <= y[1] or y[0] >= end >= y[1]:
                min = y[0] if y[0] < start else start
                max = y[1] if y[1] > end else end
                print('min max', min, max)
                total.remove((y[0], y[1]))
                if (start, end) in total:
                    total.remove((start, end))
                total.add((min, max)) # Add() method don't add element to the end 
                print('true', total)
            else:
                print('else', total, '+', start, end)
                total.add((start, end))

    s = sum(list(map(lambda x: x[1] - x[0], total)))
    return total, s


if __name__=='__main__':
    x = [
        [1, 4],
        [7, 10],
        [3, 5],
    ]
    # 986
    x = [(-493, 17), (-438, 385), (-159, -74), (-114, -23), (-73, 289), (-24, 465), (-22, 283), (69, 193), (111, 434), (159, 281), (185, 205), (192, 392), (196, 255), (203, 468), (249, 384), (261, 421), (300, 493), (359, 493)]
    # 887
    x = [(-485, 123), (-414, -200), (-372, 58), (-371, -98), (-330, 87), (-231, 8), (-22, 184), (42, 236), (134, 216), (320, 444), (368, 486), (403, 485), (435, 463)]
    # 916
    # x = [(-444, 144), (-320, -13), (-224, -133), (-146, -116), (-92, 387), (54, 339), (108, 472), (204, 420), (226, 316), (233, 408), (256, 410)]


    print(sum_of_intervals(x))
