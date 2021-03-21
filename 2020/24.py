from time import time
from common import read

directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']
ops = {'w' : 'e', 'sw': 'ne', 'se': 'nw'}
        # 'e': 'w', 'sw': 'ne', 'nw': 'se'}
eqs = {'e': ['se', 'ne'],\
       'w': ['sw', 'nw'],\
       'se': ['e', 'sw'],\
       'sw': ['w', 'se'],\
       'nw': ['w', 'ne'],\
       'ne': ['e', 'nw']}

def split(l):
    moves = [] 
    chars = list(l)
    # print(chars)
    while chars:
        c = chars.pop(0)
        if c in ['e', 'w']:
            moves.append(c)
        else:
            moves.append(c+chars.pop(0))
    return moves

def key_cnt(arr):
    return {v: arr.count(v) for v in arr}

def cancel(dmap):
    for k,v in ops.items():
        if dmap.get(k) and dmap.get(v):
            if dmap[k] > dmap[v]:
                dmap[k] = dmap[k] - dmap[v]
                dmap[v] = 0
            else:
                dmap[v] = dmap[v] - dmap[k]
                dmap[k] = 0
    return dmap

def subs(dmap):
    for k, vals in eqs.items():
        first, second = vals
        first_val = dmap.get(first)
        second_val = dmap.get(second)
        if first_val and second_val:
            diff = min(first_val, second_val)
            if k not in dmap:
                dmap[k] = 0
            dmap[k] += diff
            dmap[first] -= diff
            dmap[second] -= diff
    return dmap

def join(dmap):
    return ''.join([d*dmap.get(d) for d in directions if dmap.get(d)])

def short_path(s):
    return join(subs(cancel(subs(key_cnt(split(s))))))

assert short_path('esew') == 'se'
assert short_path('nwwswee') == ''

def black_tile_cnt(inp):
    return list(key_cnt([short_path(s) for s in inp.split('\n')]).values()).count(1)

def get_black_tiles(inp):
    return [t for t, c in key_cnt([short_path(s) for s in inp.split('\n')]).items() if c == 1]

def update(black_tiles):
    updated_black = set()
    for bt in black_tiles:
        neighbors = [short_path(bt+d) for d in directions]
        # print('neighbors : ', bt, [(bt+d, short_path(bt+d)) for d in directions])
        black_neighbors = list(filter(lambda n: n in black_tiles, neighbors))
        if 0 < len(black_neighbors) <= 2:
            updated_black.add(bt)
        for n in set(neighbors) - set(black_neighbors) - set(updated_black):
            # if n not in black_tiles:
            secondary_neighbors = [short_path(n+d) for d in directions]
            
            secondary_black_neighbors = list(filter(lambda n: n in black_tiles, secondary_neighbors))
            if len(secondary_black_neighbors) == 2:
                updated_black.add(n)
    return updated_black


def iterate(inp, it=10):
    black_tiles = set(get_black_tiles(inp))
    print('days : ', len(black_tiles))
    for i in range(it):
        black_tiles = update(black_tiles)
        print('d : ', i+1, len(black_tiles))
    return black_tiles

ss = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".strip()

inp = read('24.txt').strip()

# print(len([short_path(s) for s in ss.split('\n')]))
# print(([short_path(s) for s in ss.split('\n')]))
# print(key_cnt([short_path(s) for s in inp.split('\n')]))

# part 1
# print(black_tile_cnt(inp))

# part 2
t = time()
print(len(iterate(inp, 100)))
print('time : ', time()-t)
