# better solution from https://github.com/norvig/pytudes/blob/master/ipynb/Advent-2020.ipynb

from itertools import product, chain
from functools import lru_cache
from collections import Counter
import operator
# 322
# 2000

flatten = chain.from_iterable

Picture = """
#....#.#
..##.##.
#..#..#.
.#..#..#
.#..#...
##.#####
#..#..#.
##.##..#
""".strip().split('\n')

def day17_1(picture, d=3, n=6):
    pass

@lru_cache()
def cell_deltas(d):
    return set(filter(any, product((-1, 0, 1), repeat=d)))

def neighbors(cell):
    return [tuple(map(operator.add, cell, delta))
            for delta in cell_deltas(len(cell))]

def neighbor_counts(cells):
    return Counter(flatten(map(neighbors, cells)))

def next_generation(cells):
    return {cell for cell, count in neighbor_counts(cells).items() if count == 3 or (count == 2 and cell in cells)}

def life(cells, n):
    for g in range(n):
        cells = next_generation(cells,)
    return cells

def parse_cells(picture, d=3, active='#'):
    return {(x,y, *(0,) * (d-2))
            for (y, row) in enumerate(picture)
            for x, cell in enumerate(row) if cell is active}

def day17_1(picture, d=3, n=6):
    return len(life(parse_cells(picture, d), n))

print('---')
print(day17_1(Picture))
print(day17_1(Picture, d=4))

