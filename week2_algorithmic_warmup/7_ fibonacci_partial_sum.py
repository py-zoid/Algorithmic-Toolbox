# Uses python3
import sys

# Fast Algorithm ############################################
#############################################################
def fib_sum(n):
    mod_seq = []
    mod_seq.append(0)
    mod_seq.append(1)
    mod_seq.append(2)
    p = 2
    while not(mod_seq[p-1] == 0 and mod_seq[p] == 1):
        mod_seq.append((mod_seq[p] + mod_seq[p-1]+1) % 10)
        p = p + 1

    l = n % (p-1)
    return (mod_seq[l])


# Main Function ############################################
############################################################
if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    m = fib_sum(from_ - 1)
    n = fib_sum(to)
    d = n - m
    if d < 0:
        d = 10 + d
        print(d)
    else:
        print(d)