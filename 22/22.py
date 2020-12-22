import fileinput
from collections import deque
from itertools import islice

p1, p2 = ''.join(fileinput.input()).split('\n\n')
d1 = deque(map(int, p1.splitlines()[1:]))
d2 = deque(map(int, p2.splitlines()[1:]))

def game_1(d1, d2):
    while d1 and d2:
        c1, c2 = d1.popleft(), d2.popleft()
        if c1 > c2:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)

    winner = d1 if d1 else d2
    return winner

winner = game_1(d1.copy(), d2.copy())
print(sum(card * mult for card, mult in zip(winner, range(len(winner), 0, -1))))

def game_2(d1, d2):
    memo = set()

    while d1 and d2:
        td1, td2 = tuple(d1), tuple(d2)
        if (td1, td2) in memo:
            return 1, d1
        memo.add((td1, td2))
        
        c1, c2 = d1.popleft(), d2.popleft()
        if c1 <= len(d1) and c2 <= len(d2):
            w, _ = game_2(deque(islice(d1, c1)), deque(islice(d2, c2)))
        else:
            w = 1 if c1 > c2 else 2
        
        if w == 1:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)

    w = 1 if d1 else 2
    return w, d1 if d1 else d2

w, d = game_2(d1, d2)
print(sum(card * mult for card, mult in zip(d, range(len(d), 0, -1))))