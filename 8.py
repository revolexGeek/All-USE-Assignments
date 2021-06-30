import itertools

a = itertools.product('ABCD', repeat=4)

counter = 1
for x in a:
  print(counter, ''.join(x))
  counter += 1
