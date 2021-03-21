from time import time
from common import lines

adjcoord = [(x,y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]

def neighbors(grid, coord):
    (cx, cy) = coord
    return [grid[cx+nx][cy+ny] if 0 <= cx+nx < len(grid) and 0<= cy+ny < len(grid[0]) else '.' for nx, ny in adjcoord]

def neighborsB(grid, coord):
    (cx, cy) = coord
    neigh = []
    for [nx, ny] in adjcoord:
        ux, uy = cx, cy
        while True:
            ux, uy = ux+nx, uy+ny
            if ux < 0 or ux >= len(grid) or uy < 0 or uy >= len(grid[0]):
                neigh.append('.')
                break
            elif grid[ux][uy] == '#' or grid[ux][uy] == 'L':
                neigh.append(grid[ux][uy])
                break
    return neigh

def iter(grid, neighfun, occupiedLimit):
    newgrid = []
    for xi in range(len(grid)):
        newgrid.append('')
        for yi in range(len(grid[0])):
            seat = grid[xi][yi]
            if seat != '.':
                neigh = neighfun(grid, (xi, yi))
                if seat == 'L' and neigh.count('#') == 0:
                    seat = '#'
                elif seat == '#' and neigh.count('#') >= occupiedLimit:
                    seat = 'L'
            newgrid[xi] += seat
    return newgrid

def to_str(grid):
    return '\n'.join(grid)

def is_same(grid, othergrid):
    return to_str(grid) == to_str(othergrid)

def A(grid):
    while True:
        newgrid = iter(grid, neighbors, 4)
        if is_same(grid, newgrid):
            return to_str(newgrid).count('#')
        grid = newgrid

def B(grid):
    while True:
        newgrid = iter(grid, neighborsB, 5)
        if is_same(grid, newgrid):
            return to_str(newgrid).count('#')
        grid = newgrid

s1 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".strip().split('\n')

assert A(s1) == 37
assert B(s1) == 26

if __name__ == '__main__':
    t = time()
    print(A(lines('11.txt')))
    t1 = time()
    print('time A : ', t1 - t)
    print(B(lines('11.txt')))
    print('time B : ', time() - t)

