# Uses python3
import sys

def get_optimal_value(n, cap, weights, values):
    value = 0
    index = 0
    val_by_wt = []
    for i in range(0, n):
        val_by_wt.append(values[i] / weights[i])
    while ((cap > 0)and(n > 0)):
        max_val = 0
        for i in range(0, n):
            if val_by_wt[i] > max_val:
                max_val = val_by_wt[i]
                index = i
        val_by_wt.remove(max_val)
        fraction = weights.pop(index)
        n = n - 1
        if cap >= fraction:
            value = value + values.pop(index)
            cap = cap - fraction
        else:
            value = value + max_val * cap
            cap = 0

    return value


if __name__ == "__main__":
    data = list(map(int, (sys.stdin.read().split())))
    flag = 0
    n, capacity = data[0:2]
    if (n >=1 and capacity >= 0):
        values = data[2:(2 * n + 2):2]
        weights = data[3:(2 * n + 3):2]
        for i in range (0, n):
            if (values[i] < 0 or weights[i] <= 0):
                flag = 1
        if flag == 0:
            opt_value = (get_optimal_value(n, capacity, weights, values))
            print("{:.4f}".format(opt_value))