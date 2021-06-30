def getDells(n):
    dells = []
    for x in range(2, n):
        if n % x == 0:
            dells.append(x)
    if len(dells) < 2:
        return 0
    return dells[0] + dells[-1]


for i in range(452022, 999999999999999):
    if getDells(i) % 7 == 3:
        print(i, getDells(i))
