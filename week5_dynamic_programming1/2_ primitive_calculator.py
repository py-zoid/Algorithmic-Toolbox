# Uses python3
import sys

def optimal_sequence(n):
    sequence = [0]*(n+1)
    path = [0]*(n+1)
    k = 2
    while k <= n:
        m1 = sequence[k-1] + 1

        if k % 2 == 0:
            m2 = sequence[int(k/2)] + 1
        else:
            m2 = n

        if k % 3 == 0:
            m3 = sequence[int(k/3)] + 1
        else:
            m3 = n

        minim = min(m1, m2, m3)

        if minim == m1:
            sequence[k] = m1
            path[k] = 1
        elif minim == m2:
            sequence[k] = m2
            path[k] = 2
        else:
            sequence[k] = m3
            path[k] = 3
        k += 1

    l = n
    track = [n]
    while l > 1:
        if path[l] == 3:
            l = int(l/3)
            track.append(l)
        elif path[l] == 2:
            l = int(l/2)
            track.append(l)
        else:
            l = l - 1
            track.append(l)

    return sequence, reversed(track)

# def optimal_sequence(n):
#     sequence = [0]*n
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = [1]
sequence, track = optimal_sequence(n)
print(sequence[-1])
for a in track:
    print(a, end=' ')
