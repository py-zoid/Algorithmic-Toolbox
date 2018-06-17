# Uses python3

def calc_fib(n):
    global seq
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq[n-1]

n = int(input())
if (n>=0 and n <= 45):
    seq = []
    seq.append(1)
    seq.append(1)
    print (calc_fib(n))