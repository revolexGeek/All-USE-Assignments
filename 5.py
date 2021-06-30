# https://inf-ege.sdamgia.ru/problem?id=8094

def getBin(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b


def getDec(n):
    return int(n, 2)


for N in range(1, 100):
    x = getBin(N)
    b = 0
    for i in x:
        b += int(i)
    if b % 2 == 0:
        x += '0'
    else:
        x += '1'
    b = 0
    for i in x:
        b += int(i)
    if b % 2 == 0:
        x += '0'
    else:
        x += '1'
    print(getDec(x), x)
