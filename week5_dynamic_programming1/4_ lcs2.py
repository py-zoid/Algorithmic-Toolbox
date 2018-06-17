#Uses python3

import sys

def lcs2(n, a, m, b):

    lsm = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                lsm[i][j] = lsm[i-1][j-1] + 1
            elif a[i-1] != b[j-1]:
                lsm[i][j] = max(lsm[i-1][j-1], lsm[i-1][j], lsm[i][j-1])

    return lsm[n][m]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(n, a, m, b))