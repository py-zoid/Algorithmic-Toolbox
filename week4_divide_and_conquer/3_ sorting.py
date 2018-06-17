# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    p = l
    q = l+1

    for i in range(l+1, r+1):
        if a[i] < x:
            a.insert(p, a.pop(i))
            p += 1
            q += 1
        elif a[i] == x:
            a.insert(q, a.pop(i))
            q += 1
    return p, q



def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    if k > l:
        a[k], a[l] = a[l], a[k]
    p, q = partition3(a, l, r)
    randomized_quick_sort(a, l, p)
    randomized_quick_sort(a, q, r)

# if __name__ == '__main__':
#     inp = sys.stdin.read()
#     n, *a = list(map(int, inp.split()))
#     if n <= 100000 and n > 0:
#         randomized_quick_sort(a, 0, n - 1)
#         for x in a:
#             print(x, end=' ')


########## Stress test #1 #########################
a = ([555555555]*20000 + [5555555555]*20000 + [5555555555]*10000 + [5555555555]*20000 + [5555555555]*20000 + [5555555555]*10000)
c = ([555555555]*20000 + [5555555555]*20000 + [5555555555]*10000 + [5555555555]*20000 + [5555555555]*20000 + [5555555555]*10000)
n = 100000
while a == c:
    a = ([555555555]*20000 + [5555555555]*20000 + [5555555555]*10000 + [5555555555]*20000 + [5555555555]*20000 + [5555555555]*10000)
    randomized_quick_sort(a, 0, n - 1)
    print('correct output')
print('wrong output')


########## Stress test #2 #########################
# a = [0]*10
# p = 10
# for i in range(0, 10):
#     a[i] = i+1
# c = [0]*10
# for i in range(0, 10):
#     c[i] = i+1
# print('c done')
# n = 10
# while a == c:
#     for i in range(0, 10):
#         a[i] = p - i
#     print(a)
#     print('a done')
#     randomized_quick_sort(a, 0, n - 1)
#     print('correct output')
#     print(a)
# print('wrong output')
# print(a)