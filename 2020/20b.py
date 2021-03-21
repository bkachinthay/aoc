from re import findall
from copy import deepcopy
from common import read
from time import time

pic = """
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###
""".strip()

def split(p):
    return [[c for c in l] for l in p.strip().split('\n')]

def join(p):
    return '\n'.join([''.join(l) for l in p])

def rotate(p):
    lines = list(reversed(split(p)))
    new_lines = []
    for i in range(len(lines[0])):
        new_lines.append([l[i] for l in lines])
    return join(new_lines)

def flip(p, vertical=False):
    return join([list(reversed(l)) for l in split(p)] if vertical \
            else list(reversed(split(p))))

# rotating 4 times clockwise should give same result
assert rotate(rotate(rotate(rotate(pic)))) == pic
assert flip(flip(pic)) == pic
assert flip(flip(pic, True), True) == pic


def sides(p_in):
    p = split(p_in)
    return { 'N': p[0], 'S': p[-1], 'E': ''.join([l[-1] for l in p]), 'W': ''.join([l[0] for l in p])}

compare = { 'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E' }

def relative_pos(p1, p2):
    s1 = sides(p1)
    s2 = sides(p2)
    for k, v in compare.items():
        if s1[k] == s2[v]:
            return ((1 if k == 'E' else ( -1 if k == 'W' else 0)),\
                (1 if k == 'N' else ( -1 if k == 'S' else 0)))
    return False

# tile = [rotated_pixed, rotate_count, [grid_x, grid_y]]
def get_pos(t1, otherp):
    (pkey2, p2) = otherp
    [pkey, p1, r1, [gx1, gy1]] = t1
    p2_tmp = deepcopy(p2)
    for ri in range(4):
        rel = relative_pos(p1, p2_tmp)
        if rel:
            return [pkey2, p2_tmp, ri, [gx1 + rel[0], gy1 + rel[1]]]
        p2_tmp = rotate(p2_tmp)
    p2_flip = flip(deepcopy(p2))
    for ri in range(4):
        rel = relative_pos(p1, p2_flip)
        if rel:
            return [pkey2, p2_flip, 4+ri, [gx1 + rel[0], gy1 + rel[1]]]
        p2_flip = rotate(p2_flip)
    p2_vert_flip = flip(deepcopy(p2), True)
    for ri in range(4):
        rel = relative_pos(p1, p2_vert_flip)
        if rel:
            return [pkey2, p2_vert_flip, 8+ri, [gx1 + rel[0], gy1 + rel[1]]]
        p2_vert_flip = rotate(p2_vert_flip)
    return False

s = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""

def parse_tile(t):
    num, grid = t.split(':')
    return (findall('\d+', num)[0], grid.strip())

def patch(tiles):
    patched = [[tiles[0][0], tiles[0][1], 0, [0, 0]]]
    remaining = tiles[1:]
    while remaining:
        rem = remaining.pop(0)
        for px in patched:
           rp_pos = get_pos(px, rem)
           if rp_pos:
               patched.append(rp_pos)
               break
        else:
            remaining.append(rem)
    return patched

def get_x_range(points):
    return  [min([p[1][0] for p in points]), max([p[1][0] for p in points])]

def get_y_range(points):
    return [min([p[1][1] for p in points]), max([p[1][1] for p in points])]

def corners(points):
    possiblex = get_x_range(points)
    possibley = get_y_range(points)
    return [p[0] for p in points if p[1][0] in possiblex and p[1][1] in possibley]

def points(patched):
    return [(p[0], p[-1]) for p in patched]

def prod(nums):
    pr = 1
    for n in nums:
        pr *= int(n)
    return pr

# part A

# tiles = [parse_tile(t) for t in s.split('\n\n')]
# print(get_pos([tiles[5][0], tiles[5][1], 0, [0, 0]], tiles[2]))

tiles = [parse_tile(t) for t in read('20.txt').split('\n\n')]
# print(len(tiles), patch(tiles))
# t = time()
# t2 = time()
# print(prod(corners(points(patch(tiles)))))
# t3 = time()
# print('time took A: ', t3 - t)

def grange(rng):
    a,b = rng
    return range(a,b+1)

def patch_dict(patched):
    return {p[0]: p for p in patched}

def get_id(mapped, coord):
    return 

# def join(arr, d=''):
#     print(arr)
#     return d.join(arr)

def merge_lines(gline):
    lines = [split(t[1]) for t in gline]
    return '\n'.join([''.join([''.join(t[li][1:-1]) for t in lines])\
            for li in range(len(lines[0]))\
            if li != 0 and li != len(lines[0]) - 1])

# part B
def stitch(tiles):
    patched = patch(tiles)
    pts = points(patched)
    x_range = get_x_range(pts)
    y_range = get_y_range(pts)
    minx = x_range[0]
    maxy = y_range[1]
    grid = [[None for x in grange(x_range)]\
            for y in grange(y_range)]
    for p in patched:
        gx, gy = p[-1]
        grid[maxy-gy][gx-minx] = p
    s = '\n'.join([merge_lines(gline) for gline in grid])
    return s

snake_str = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

snake = [[c for c in l] for l in snake_str.split('\n')]
snake_len = len(snake[0])
snake_height = len(snake)

def replace_snake(grid):
    grid_x = len(grid[0])
    grid_y = len(grid)
    new_grid = deepcopy(grid)
    for y in range(grid_y):
        for x in range(grid_x):
            if (x+snake_len) >= grid_x or (y+snake_height) >= grid_y:
                break
            is_snake = True
            for sy in range(snake_height):
                for sx in range(snake_len):
                    if snake[sy][sx] == '#' and grid[y+sy][x+sx] == '.':
                        is_snake = False
                        break
                if not is_snake:
                    break
            if is_snake:
                for sy in range(snake_height):
                    for sx in range(snake_len):
                        if snake[sy][sx] == '#':
                            new_grid[y+sy][x+sx] = 'O'
    return new_grid
                
def rplc_snake(gstr):
    return join(replace_snake(split(gstr)))

def combs(grid):
    cnts = []
    new_grid = rplc_snake(grid)
    cnts.append(new_grid.count('#'))
    for ri in range(3):
        new_grid = rplc_snake(rotate(new_grid))
        cnts.append(new_grid.count('#'))
    new_grid = rplc_snake(flip(grid))
    for ri in range(3):
        new_grid = rplc_snake(rotate(new_grid))
        cnts.append(new_grid.count('#'))
    new_grid = rplc_snake(flip(grid, True))
    for ri in range(3):
        new_grid = rplc_snake(rotate(new_grid))
        cnts.append(new_grid.count('#'))
    return min(cnts)

gg = stitch(tiles)
print('--- part B ---')
print('YYY : ', combs(gg))
print('----------------------------------------')
