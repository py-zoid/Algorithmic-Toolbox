# Uses python3
import sys

def get_change(m):
    k = 1
    n = [0]*(m+1)
    while k <= m:
        if k >= 4:
            n[k] = min(n[k-1] + 1, n[k-3] + 1, n[k-4] + 1)
        elif k == 3:
            n[k] = min(n[k - 1] + 1, n[k - 3] + 1)
        else:
            n[k] = n[k-1] + 1
        k += 1
    return n[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
