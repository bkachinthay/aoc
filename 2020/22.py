from time import time
from common import mapl, read

s = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

def decks(s):
    parse_deck = lambda d: mapl(int, (d.split('\n'))[1:])
    return mapl(parse_deck, s.split('\n\n'))

def score(arr):
    def _score(vals):
        x,y = vals
        return (x+1) * y
    return sum(map(_score, enumerate(reversed(arr))))

def part1(s):
    deck1, deck2 = decks(s)
    while deck1 and deck2:
        d1 = deck1.pop(0)
        d2 = deck2.pop(0)
        if d1 > d2:
            deck1 += [d1, d2]
        else:
            deck2 += [d2, d1]
    winner = deck1 or deck2
    return score(winner)

def part2(s):
    deck1, deck2 = decks(s)
    ndeck1, ndeck2 = _part2(deck1, deck2)
    return score(ndeck1 or ndeck2)

def join(arr):
    return ','.join(map(str, arr))

def _part2(deck1, deck2):
    cache_deck1, cache_deck2 = set(), set()
    winner = 1
    d1, d2 = None, None
    while True:
        if not deck1 or not deck2:
            return deck1, deck2
        elif join(deck1) in cache_deck1 or join(deck2) in cache_deck2:
            winner = 1
            cache_deck1.add(join(deck1))
            cache_deck2.add(join(deck2))
            d1 = deck1.pop(0)
            d2 = deck2.pop(0)
        else: 
            cache_deck1.add(join(deck1))
            cache_deck2.add(join(deck2))
            d1 = deck1.pop(0)
            d2 = deck2.pop(0)
            if d1 <= len(deck1) and d2 <= len(deck2):
                new_deck1, new_deck2 = _part2(deck1[:d1], deck2[:d2])
                if new_deck1:
                    winner = 1
                else:
                    winner = 2
            elif d1 > d2:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            deck1 += [d1, d2]
        else:
            deck2 += [d2, d1]

inp = read('22.txt').strip()
print(part1(s))
print(part1(inp))
print('--- part 2 ---')
t = time()
# print(part2(s))
print(part2(inp))
print('time took ', time()-t)
