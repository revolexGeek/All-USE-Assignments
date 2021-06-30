A = 1

while True:
    for x in range(1000):
        for y in range(1000):
            if not ((y + 2 * x != 48) or (A < x) or (A < y)):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1
