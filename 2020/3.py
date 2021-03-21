from common import lines

def A(fname, c_inc, r_inc):
    rows = lines('3a.txt')
    col_len = len(rows[0])
    tree_cnt = 0
    c = 0
    for row in rows[::r_inc]:
        tree_cnt += row[c%col_len] == '#'
        c += c_inc;
    return tree_cnt

def B(fname):
    return A(fname, 1, 1) *\
            A(fname, 3, 1) *\
            A(fname, 5, 1) *\
            A(fname, 7, 1) *\
            A(fname, 1, 2)


if __name__ == "__main__":
    print( A('3a.txt', 3, 1))
    print( B('3a.txt'))

