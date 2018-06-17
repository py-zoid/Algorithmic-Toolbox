# Uses python3
import sys
import random

def inpt_stress():
    starts_num = []
    ends_num = []
    points = []
    for i in range(0, 5):
        s = random.randint(0, 49)
        e = random.randint(s+1, 50)
        starts_num.append(s)
        ends_num.append(e)
    for i in range (0, 5):
        p = random.randint(0, 49)
        points.append(p)
    return starts_num, ends_num, points

# def partition3(arr, l, r):
#     x = arr[l][0]
#     j = l
#     k = l + 1
#     for i in range(l + 1, r + 1):
#         if arr[i][0] == x:
#             j += 1
#             arr[i], arr[j] = arr[j], arr[i]
#         elif arr[i][0] < x:
#             j += 1
#             arr[i], arr[j] = arr[j], arr[i]
#             arr[k], arr[j] = arr[j], arr[k]
#             k += 1
#     arr[l], arr[k-1] = arr[k-1], arr[l]
#     return k, j
#
# def randomized_quick_sort(arr, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     arr[l], arr[k] = arr[k], arr[l]
#     p, q = partition3(arr, l, r)
#     randomized_quick_sort(arr, l, p-1)
#     randomized_quick_sort(arr, q+1, r)

def count_segments(arr, m):
    result = [0]*m
    st = 0
    en = 0
    for point in arr:
        # print('point = ' + str(point),end=' ')
        if point[1] == 0:
            st += 1
        elif point[1] == m+4:
            en += 1
        else:
            # print(st, en)
            result[point[1] - 2] = st - en
            # print(result)
    return result

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    # g = [0]
    # h = [0]
    # while(g == h):
    #print('success')
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    m = data[1]
    # n = 5
    # m = 5
    starts_num = data[2:2 * n + 2:2]
    start_values = [0] * n
    ends_num = data[3:2 * n + 2:2]
    end_values = [m+4] * n
    # starts_num, ends_num, points_num = inpt_stress()
    points_num = data[2 * n + 2:]
    points_values = []
    for i in range(2, m+2):
        points_values.append(i)
    points = zip(points_num, points_values)
    starts = zip(starts_num, start_values)
    ends = zip(ends_num, end_values)
    points = list(points)
    starts = list(starts)
    ends = list(ends)
    arr = starts + points + ends
    arr.sort()
    # print(arr)
    result = count_segments(arr, m)
    for r in result:
        print(r, end=' ')
#     g = count_segments(arr, m)
#     print('g done')
#     h = naive_count_segments(starts_num, ends_num, points_num)
# print('wrong output')
# print(starts_num)
# print(ends_num)
# print(points_num)
# print(arr)
# print(g)
# print(h)
