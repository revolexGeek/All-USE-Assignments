from functools import lru_cache


def moves(h):
    a, b = h
    return (a, b + 1), (a, (b * 3) - 1)


@lru_cache(None)
def game(h):
    if sum(h) >= 33:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'B2'


for i in range(1, 32 + 1):
    if game((0, i)) is not None:
        print(i, game((0, i)))
