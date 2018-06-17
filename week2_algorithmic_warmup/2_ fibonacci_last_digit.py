# Uses python3
import sys

#Fast Algorithm######################################
#####################################################

def last_digit(n):
    """this fucntion gives out the last digit of a number"""

    return n % 10

def last_fib_digit(n):
    """This function creates the """

    # global seq
    seq = []
    seq.append(1)
    seq.append(1)

    if n <= 2:
        return(1)

    for i in range(2, n):
        seq.append(last_digit(seq[i-1] + seq[i-2]))

    return seq[n-1]

# Main function########################################
#######################################################
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    seq = []
    seq.append(1)
    seq.append(1)
    if (n >= 0 and n <= 10000000):
        print(last_fib_digit(n))
