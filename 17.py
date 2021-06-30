a = [x for x in range(3361, 9205+1) if (x % 4 == 0 or x % 5 == 0) and (x % 9 != 0 and x % 11 != 0 and x % 17 != 0 and x % 23 != 0)]
print(len(a), max(a))

# или этот вариант (фу)

'''counter, m = 0, 99999999999

for i in range(4668, 10414 + 1):
    if (i % 3 == 0 or i % 11 == 0) and (i % 2 != 0 and i % 13 != 0 and i % 22 != 0 and i % 33 != 0):
        counter += 1
        m = min(m, i)

print(counter, m)'''

