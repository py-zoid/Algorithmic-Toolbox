# Uses python3
import sys

def get_change(m):
    n = 0
    iter = 0
    while (m != 0):
        if iter == 2:
            n = n + m
            m = 0
        elif iter == 1:
            fives = m // 5
            n = n + fives
            m = m % 5
            iter = 2
        else:
            tens = m // 10
            n = n + tens
            m = m % 10
            iter = 1
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))