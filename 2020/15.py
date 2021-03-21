from time import time 

def parse(s):
    return list(map(int, s.strip().split(',')))

def A(vals, til=2020):
    cmap = {}
    i = 1
    for v in vals:
        if v in cmap:
            cmap[v].append(i)
        else:
            cmap[v] = [i]
        # print('itrr : ', i, v)
        i += 1
    last_spoken = vals[-1]
    while i <= til:
        if len(cmap[last_spoken]) > 1:
            a,b = cmap[last_spoken][-2:]
            last_spoken = b - a
        else:
            last_spoken = 0
        if last_spoken not in cmap:
            # cmap[last_spoken].append(i)
            cmap[last_spoken] = []
        # else:
        #     cmap[last_spoken] = [i]
        cmap[last_spoken].append(i)
        cmap[last_spoken] = cmap[last_spoken][-2:]
        # print('iter : ', i, last_spoken,) # cmap[last_spoken]
        i += 1
    # print(list(sorted([(k, v) for k, v in cmap.items()])))
    # print(len(list(sorted([(k, v) for k, v in cmap.items()]))))
    return last_spoken

# better implementation of A
def B(vals, til=2020):
    cmap = { v: vi+1 for vi, v in enumerate(vals)}
    curr_val = 0
    for i in range(len(vals) + 1, til):
        next_val = 0 if curr_val not in cmap else i - cmap[curr_val]
        cmap[curr_val] = i
        curr_val = next_val
    return curr_val

s1 = "0,3,6"
assert A(parse(s1)) == 436
assert A(parse("1,3,2")) == 1
assert A(parse("2,1,3")) == 10
assert A(parse("1,2,3")) == 27
assert A(parse("2,3,1")) == 78
assert A(parse("3,2,1")) == 438
assert A(parse("3,1,2")) == 1836

inp = "19,20,14,0,9,1"

if __name__ == '__main__':
    # print(A(parse(inp), 2020))
    # print(A(parse(inp), 100))
    # print(A(parse(s1), 10000))
    # print(B(parse(s1)))
    t1 = time()
    print(B(parse(inp), 30000000))
    print('time : ', time() - t1)
