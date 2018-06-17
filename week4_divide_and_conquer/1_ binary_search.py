# Uses python3
import sys

def binary_search(a, x, left, right):
    r = -1
    if left <= right:
        mid = int((left + right)/2)
        if x > a[mid]:
            left = mid + 1
            r = binary_search(a, x, left, right)
        elif x < a[mid]:
            right = mid - 1
            r = binary_search(a, x, left, right)
        else:
            r = mid
    return r

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    search_num = data[n + 2:]
    for x in search_num:
        left, right = 0, n-1
        print(binary_search(a, x, left, right), end = ' ')
