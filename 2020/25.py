def transform_till(n, sub=7):
    v = 1
    d=20201227
    for i in range(n):
        v = (v * sub) % d
    return v

def get_transform_n(val, sub=7):
    v = 1
    d=20201227
    i = 1
    while True:
        v = (v * sub) % d
        if v == val:
            return i
        i += 1

def solve(v1, v2):
    lp = get_transform_n(v1)
    return transform_till(lp, v2)

arr =[ 5764801, 17807724]

inp = [6408062, 15733400]

print(solve(*inp))

print('------------')
