#Uses python3

import sys

def lcs3(an, a, bn, b, cn, c):
    lsm = [[[0 for i in range(cn + 1)] for j in range(bn + 1)] for k in range(an + 1)]

    for i in range(1, an + 1):
        for j in range(1, bn + 1):
            for k in range(1, cn + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    lsm[i][j][k] = lsm[i - 1][j - 1][k - 1] + 1
                elif a[i - 1] != b[j - 1] or a[i -1] != c[k - 1]:
                    lsm[i][j][k] = max(lsm[i - 1][j - 1][k - 1], lsm[i - 1][j][k], lsm[i][j - 1][k], lsm[i][j][k - 1],
                                       lsm[i - 1][j - 1][k], lsm[i - 1][j][k - 1], lsm[i][j - 1][k - 1])
    return lsm[an][bn][cn]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(an, a, bn, b, cn, c))
