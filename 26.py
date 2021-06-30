f = open('26.txt')

s, n = map(int, f.readline().split())

a = [int(f.readline()) for m in range(1, n + 1)]
a.sort()

b = []
for x in range(len(a)):
    if sum(b) + a[x] <= s:
        b.append(a[x])

k = -1
while sum(b) < s:
    m = 0
    for x in a:
        if x <= b[k] + (s - sum(b)):
            m = x
    b[k] = m
    k -= 1

print(len(b), max(b))