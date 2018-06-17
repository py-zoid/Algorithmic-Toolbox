# Uses python3
import sys

# Fast Algorithm #################################
##################################################
def lcm(a, b):
    reminder = 1
    gcd = 1
    c = a
    d = b
    while (reminder != 0):
        if c > d:
            reminder = c % d
            gcd = d
            c = reminder

        else:
            reminder = d % c
            gcd = c
            d = reminder
    ans = int(b / gcd)
    ans = a * ans
    return ans

# main function ###############################################
###############################################################
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if (a >= 1 and b >= 1 and a <= 2000000000 and b <= 2000000000):
        print(lcm(a, b))