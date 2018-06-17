# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
m_1 = 0;
m_2 = 0;
for i in range(0, n):

    if (a[i] >= m_1):
        m_2 = m_1
        m_1 = a[i]

    elif (a[i] > m_2 and a[i] < m_1):
        m_2 = a[i]

    result = m_1 * m_2

print(result)
