import re
from itertools import product
from common import read 

def bin36(n):
    return bin(n)[2:].zfill(36)

def apply_mask(n, m):
    return ''.join([mb if mb != 'X' else nb for nb, mb in zip(n,m)])
    # return [(nb, mb) for nb, mb in zip(n,m)]

def A(inp):
    mask = ''
    mem = {}
    for l in inp.strip().split('\n'):
        a,b = l.replace(' ', '').split('=')
        if a == 'mask':
            mask = b
        else:
            k, _ = re.subn('[mem\[\]]', '', a)
            mem[k] = int(apply_mask(bin36(int(b)), mask), 2)
    return sum(mem.values())

def apply_mask2(n, m):
    return ''.join([(('1' if mb == '1' else nb) if mb != 'X' else 'X') for nb, mb in zip(n,m)])

def replace(m, vals):
    for v in vals:
        m = m.replace('X', str(v), 1)
    return m

def possible(m):
    return [replace(m, vals) for vals in product(*([[0, 1]] * m.count('X')))]

def B(inp):
    mask = ''
    possibles= {}
    for l in inp.strip().split('\n'):
        a,b = l.replace(' ', '').split('=')
        if a == 'mask':
            mask = b
        else:
            k, _ = re.subn('[mem\[\]]', '', a)
            v = apply_mask2(bin36(int(k)), mask)
            for p in possible(v):
                possibles[p] = int(b)
    return sum(possibles.values())

s1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
assert A(s1) == 165

s2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
assert B(s2) == 208

if __name__ == '__main__':
    print(A(read('14.txt')))
    print(B(read('14.txt')))
    
