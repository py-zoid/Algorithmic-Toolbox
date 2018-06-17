#Uses python3

import sys

def largest_number(n, arr):
    res = ''
    for i in range(1, n):
        index = i
        for j in range(0, i):
            a1 = int(str(arr[i])+str(arr[j]))
            a2 = int(str(arr[j])+str(arr[i]))
            if a1 > a2 and j < index:
                index = j
                break
        arr.insert(index, arr.pop(i))
    for i in range(0, n):
        res += str(arr[i])
    return res


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = (data[0])
    arr = data[1:]
    bool = 1
    for val in arr:
        if (((val)<1) or (int(val)>1000)):
            bool = 0
            break
    if ((bool == 1) and (n>=1) and (n<=100)):
        print(largest_number(n, arr))