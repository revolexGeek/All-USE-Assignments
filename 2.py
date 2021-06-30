# ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y)
# https://inf-ege.sdamgia.ru/problem?id=28538

print('X Y Z W')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((x and y) <= ((not z) or w)) and (((not w) <= x) or (not y))):
                    print(x, y, z, w)
