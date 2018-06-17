#Uses python3
import sys
import math

def minimum_distance(l, r, points):
    midx = int(n/2)
    d1 = minimum_distance(l, midx, points[l: midx + 1])
    d2 = minimum_distance(n-midx, r, points[midx + 1 : r])
    d = min(d1, d2)
    intersection = []
    for i in range(l, r):
        if 0 <= midx - points[i][0] <= d or 0 <= points[i][0] - midx <= d:
            intersection.append(points[i])



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    print(n)
    x = data[1::2]
    print(x)
    y = data[2::2]
    print(y)
    points = zip(x, y)
    points = list(0, n, points)
    points.sort()
    print(points)
    # print("{0:.9f}".format(minimum_distance(points)))