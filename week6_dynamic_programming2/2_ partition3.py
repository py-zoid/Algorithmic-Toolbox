# Uses python3
import sys
import itertools

def partition3(A, n, sum, p):
    sum1 = [[0 for i in range(sum+1)] for j in range(n+1)]
    for i in range(0, n+1):
        sum1[i][0] = (i+1)*n

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if sum1[i-1][j] >0 and j != sum:
                sum1[i][j] = sum1[i-1][j]
            if A[i-1] <= j:
                if sum1[i-1][j-A[i-1]] > 0:
                    sum1[i][j] = sum1[i-1][j-A[i-1]] + 1

    diff = 0
    for i in range(1, n+1):
        if sum1[i][sum] != sum1[i-1][sum]:
            diff += 1
    if diff >= 3:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    sum = 0
    for i in A:
        sum += i
    if sum % 3 == 0:
        sum = int(sum / 3)
        print(partition3(A, n, sum, 1))
    else:
        print('0')

