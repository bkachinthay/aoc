from common import lines

def seatID(code):
    row = code[:7].replace('B', '1').replace('F', '0')
    col = code[7:].replace('R', '1').replace('L', '0')
    return sum([int(r) * 2 ** p for (r, p) in zip(row, reversed(range(7)))]) * 8\
            + sum([int(c) * 2 ** p for (c, p) in zip(col, reversed(range(3)))])

assert seatID('BFFFBBFRRR') == 567
assert seatID('FFFBBBFRRR') == 119
assert seatID('BBFFBBFRLL') == 820

def A(fname):
    return max([seatID(l) for l in lines(fname)])

def B(fname):
    occupied = {seatID(l) for l in lines(fname)}
    return [s for s in range(128 * 8)\
            if s not in occupied and (s-1) in occupied and (s+1) in occupied]

if __name__ == '__main__':
    print(A('5.txt'))
    print(B('5.txt'))

