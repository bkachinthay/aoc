import re
from common import mapl 

s = """Tile 2311:
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
..#.###..."""

def edges(img):
    return {'t': img[0], 'l': ''.join([im[0] for im in img]), 'r': ''.join([im[-1] for im in img]), 'b': img[-1]}

def clockwise(img):
    num, pixels, edges = img
    new_pixels = [[] for _ in range(len(pixels[0]))]
    for p in pixels:
        for pi, pv in enumerate(p):
            new_pixels[pi].append(pv)
    return num, [''.join(p) for p in new_pixels], { 't': edges['l'], 'l': edges['b'], 'b': edges['r'], }

def parse_img(img):
    first, *rest = [i for i in img.split('\n')]
    return re.findall('\d+', first)[0], rest, edges(rest)

def parse(s):
    return mapl(parse_img, s.split('\n\n'))

def img_str(img):
    return '\n'.join(img)

def print_img(imgl):
    n, img, edgs = imgl
    print('-------')
    print(img_str(img))
    print('-------')

if __name__ == '__main__':
    i1 = parse(s)[0]
    print('before')
    print_img(i1)
    cl = clockwise(i1)
    print('after')
    print_img(cl)
    # print(parse(s))
