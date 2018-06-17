#Uses python3

import sys

def max_dot_product(n, a, b):
    # insertion sort
    for i in range (1, n):
        for j in range(0, i):
            if a[i] <= a[j]:
                a.insert(j, a.pop(i))
        for l in range(0, i):
            if b[i] <= b[l]:
                b.insert(l, b.pop(i))

    res = 0
    for i in range(0, n):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(n, a, b))