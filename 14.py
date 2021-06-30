x = 144


def getToSys(n, to):
    b = ''
    while n > 0:
        b = str(n % to) + b
        n = n // to
    return b


for i in range(2, 16):
    if len(getToSys(x, i)) >= 3 and getToSys(x, i)[len(getToSys(x, i)) - 1] == '1':
        print(i)
