from common import read

def A(inp):
    t, buses = inp.strip().split('\n')
    t = int(t)
    buses = [int(n) for n in buses.strip().split(',') if n != 'x']
    # print(t, buses)
    mint, minb = min([(b - t % b, b) for b in buses])
    return mint * minb

def B(inp):
    t, buses = inp.strip().split('\n')
    buses = buses.strip().split(',') 
    n = 0
    inc = 1
    # conditions = []
    for b, bi in zip(buses, range(len(buses))):
        if b != 'x':
            b = int(b)
            # conditions.append((b, bi))
            # while  any([(n % b1) != ((b1 - b1i) % b1) for b1, b1i in conditions]):
            while  (n % b) != ((b - bi) % b):
                n += inc
            inc *= b
    return n

s1 = """939
7,13,x,x,59,x,31,19"""
assert A(s1) == 295
assert B(s1) == 1068781

if __name__ == '__main__':
    print(A(read('13.txt')))
    print(B(read('13.txt')))
