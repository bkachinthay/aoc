from copy import deepcopy
from itertools import product
from time import time
# grid = [['.#.', ]]

def parse(s):
    return [[[c for c in l] for l in s.strip().split('\n')]]

def parseb(s):
    return [[[[c for c in l] for l in s.strip().split('\n')]]]

def line(size):
    return ['.'] * size

def plane(size):
    return [line(size) for _ in range(size)]

def cube(size, cube_size):
    return [plane(size) for _ in range(cube_size)]

def val(grid, coord, cd):
    x,y,z = (c+cd for c, cd in zip(coord,cd))
    size = len(grid[0])
    if 0 <= x < size and 0 <= y < size and 0 <= z < len(grid):
        # print('grid : ', grid)
        # print('val : ', size , x, y, z, grid[z])
        return grid[z][y][x]
    else:
        return '.'

def valb(grid, coord, cd):
    x,y,z,w = (c+cd for c, cd in zip(coord,cd))
    size = len(grid[0][0])
    if 0 <= x < size and 0 <= y < size and 0 <= z < len(grid[0]) and 0 <= w < len(grid):
        # print('valb : ', size, (x,y,z,w), grid[w][z][y][x], coord, cd, size, len(grid[0]), len(grid))
        return grid[w][z][y][x]
    else:
        return '.'

incs = [-1, 0, 1]
neighbors = [(x,y,z) for x in incs for y in incs for z in incs if x != 0 or y !=0 or z != 0 ]
neighbors4d = list(filter(lambda c: c[0] != 0 or c[1] != 0 or c[2] != 0 or c[3] != 0, product(*[incs] * 4)))

assert len(neighbors) == 26

def eval(grid, coord):
    x,y,z = coord
    vals = [val(grid, coord, c) for c in neighbors]
    cur_val = grid[z][y][x]
    if cur_val == '#' and vals.count('#') in [2,3]:
        return '#'
    elif cur_val == '.' and vals.count('#') == 3:
        return '#'
    return '.'

def evalb(grid, coord):
    x,y,z,w = coord
    # print('evalb : ', list(neighbors4d), [(coord, c) for c in neighbors4d])
    vals = [valb(grid, coord, c) for c in neighbors4d]
    # print('grid : ', grid[w][z], coord)
    cur_val = grid[w][z][y][x]
    if cur_val == '#' and vals.count('#') in [2,3]:
        return '#'
    elif cur_val == '.' and vals.count('#') == 3:
        return '#'
    return '.'

def expand(grid):
    size = len(grid[0]) + 2
    return [plane(size)] +\
             [[line(size)] +\
                [[ '.' ] + l + [ '.' ] for l in p] +\
                [line(size)] for p in grid] +\
            [plane(size)]

def expandb(grid):
    size = len(grid[0][0]) + 2
    cube_size = len(grid[0]) + 2
    return [cube(size, cube_size)] + [[plane(size)] +\
            [[line(size)] +\
            [[ '.' ] + l + [ '.' ] for l in p] +\
            [line(size)] for p in c] +\
            [plane(size)] for c in grid] + [cube(size, cube_size)]

# def expandb(grid):
#     size = len(grid[0][0]) + 2
#     return [[cube(size)] + [[plane(size)] +\
#              [[line(size)] +\
#                 [[ '.' ] + l + [ '.' ] for l in p] +\
#                 [line(size)] for p in c] +\
#             [plane(size)]] + [cube(size)] for c in grid]

def iter(grid):
    expanded_grid = expand(grid)
    new_grid = deepcopy(expanded_grid)
    for z in range(len(expanded_grid)):
        for y in range(len(expanded_grid[0])):
            for x in range(len(expanded_grid[0])):
                new_grid[z][y][x] = eval(expanded_grid, (x,y,z))
    return new_grid

def iterb(grid):
    expanded_grid = expandb(grid)
    new_grid = deepcopy(expanded_grid)
    # print('---')
    # print ('before', gstrb(grid))
    # print('===')
    # print('expanded : ', gstrb(expanded_grid))
    # print('===')
    for w in range(len(expanded_grid)):
        for z in range(len(expanded_grid[0])):
            for y in range(len(expanded_grid[0][0])):
                for x in range(len(expanded_grid[0][0][0])):
                    new_grid[w][z][y][x] = evalb(expanded_grid, (x,y,z,w))
    # print('after : ', gstrb(new_grid))
    # print('---')
    return new_grid

def A(grid):
    # print('A : ', grid)
    for i in range(6):
        grid = iter(grid)
        # print(f'-- {i} --')
        # print(gstr(grid))
    return gstr(grid).count('#')

def B(grid):
    # print('A : ', grid)
    for i in range(6):
        # print(f'-- {i} --')
        # print(gstrb(grid))
        grid = iterb(grid)
    return gstrb(grid).count('#')

def gstr(grid):
    return '\n\n'.join(['\n'.join([''.join(l) for l in p]) for p in grid])

def gstrb(grid):
    return '\n\n'.join(['\n\n'.join(['\n'.join([''.join(l) for l in p]) for p in c]) for c in grid])


s1 ="""
.#.
..#
###"""
assert A(parse(s1)) == 112

inp ="""
#....#.#
..##.##.
#..#..#.
.#..#..#
.#..#...
##.#####
#..#..#.
##.##..#"""

if __name__ == '__main__':
    # print(parse(s1))
    # print(A(parse(inp)))
    # print(B(parseb(s1)))
    t = time()
    print(B(parseb(inp)))
    print('time : ', time() - t)
    # print('neigh : ', list(filter(lambda c: c[0] != 0 or c[1] != 0 or c[2] != 0 or c[3] != 0, product(*[incs] * 4))))
