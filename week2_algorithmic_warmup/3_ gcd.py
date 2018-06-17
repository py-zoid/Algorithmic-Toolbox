# Uses python3
import sys

# fast algorithm #############################################
##############################################################

def gcd(a, b):
    reminder = 1
    ans = 1
    while (reminder != 0):
        if a > b :
            reminder = a % b
            ans = b
            a = reminder

        else:
            reminder = b % a
            ans = a
            b = reminder

    return ans

# main function ###############################################
###############################################################

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if (a >= 1 and b >= 1 and a <= 2000000000 and b <= 2000000000):
        print(gcd(a, b))