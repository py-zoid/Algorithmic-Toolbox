# Uses python3
import sys

def merge(a, left, mid, right):
    l1 = mid - left + 1
    l2 = right - mid
    L = [0] * l1
    R = [0] * l2

    for i in range(0, l1):
        L[i] = a[left + i]
    for j in range(0, l2):
        R[j] = a[mid + 1 + j]
    p = 0
    q = 0
    k = left

    while p < l1 and q < l2:
        if L[p] <= R[q]:
            a[k] = L[p]
            p += 1
        else:
            a[k] = R[q]
            q += 1
        k += 1

    if p == l1:
        for i in range(q, l2):
            a[k] = R[i]
            k += 1
    elif q == l2:
        for i in range(p, l1):
            a[k] = L[i]
            k += 1

def majority_elem(a, n):
    elem = -1
    count = 0
    for i in range(0, n):
        if a[i] == elem:
            count += 1
        elif a[i] != elem and count < n/2:
            elem = a[i]
            count = 1
        if count > n/2:
            return elem
    return -1

def mergesort(a, left, right):
    if left < right:
        mid = int((left+right)/2)
        mergesort(a, mid+1, right)
        mergesort(a, left, mid)
        merge(a, left, mid, right)

# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     elif left + 1 == right:
#         if a[left] == a[right]:
#             return a[left]
#         else:
#             return -1
#     else:
#         num1 = get_majority_element(a, int((left+right)/2)+1, right)
#         num2 = get_majority_element(a, left, int((left+right)/2))
#         if num1 == num2 and num1 != -1:
#             return num1
#         elif num1 != num2 and (num1 == -1 or num2 == -1):
#             if num1 == -1:
#                 return num2
#             else:
#                 return num1
#         else:
#             return -1

if __name__ == '__main__':
    inp = sys.stdin.read()
    n, *a = list(map(int, inp.split()))
    mergesort(a, 0, n-1)
    elem = majority_elem(a, n)
    if elem == -1:
        print('0')
    else:
        print('1')