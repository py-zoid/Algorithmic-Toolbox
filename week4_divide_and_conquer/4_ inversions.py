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
    inversions = 0

    while p < l1 and q < l2:
        if L[p] <= R[q]:
            a[k] = L[p]
            p += 1
        else:
            a[k] = R[q]
            q += 1
            inversions += l1 - p
        k += 1

    if p == l1:
        for i in range(q, l2):
            a[k] = R[i]
            k += 1
    elif q == l2:
        for i in range(p, l1):
            a[k] = L[i]
            k += 1

    return inversions

def mergesort(a, left, right):
    inversions = 0
    if left < right:
        mid = int((left+right)/2)
        inversions += mergesort(a, mid+1, right)
        inversions += mergesort(a, left, mid)
        inversions += merge(a, left, mid, right)
    return inversions

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(mergesort(a, 0, n-1))