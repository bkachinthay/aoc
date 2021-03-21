from common import numbers

s1 = """16
10
15
5
1
11
7
19
6
12
4""".strip().split('\n')

s2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".strip().split('\n')

def A(adapts):
    sadpts = list(sorted(adapts))
    adptsdiffs = [a-b for a,b in zip(sadpts + [sadpts[-1] + 3], [0] + sadpts)]
    return adptsdiffs.count(1) * adptsdiffs.count(3)

def B(adapts):
    sadpts = list(reversed(sorted(adapts)))
    sadpts = [sadpts[0] + 3] + sadpts + [0]
    ways = [1]
    for ni in range(1, len(sadpts)):
        val = 0
        val += ways[ni-1] if ni >= 1 and\
                (sadpts[ni] + 1 == sadpts[ni-1] or\
                sadpts[ni] + 2 == sadpts[ni-1] or\
                sadpts[ni] + 3 == sadpts[ni-1]) else 0
        val += ways[ni-2] if ni >= 2 and\
                (sadpts[ni] + 2 == sadpts[ni-2] or\
                sadpts[ni] + 3 == sadpts[ni-2]) else 0
        val += ways[ni-3] if ni >= 3 and\
                sadpts[ni] + 3 == sadpts[ni-3] else 0
        ways.append(val)
    return ways[-1]

assert A(list(map(int, s1))) == 7 * 5
assert A(list(map(int, s2))) == 22 * 10
assert B(list(map(int, s1))) == 8
assert B(list(map(int, s2))) == 19208

if __name__ == '__main__':
    print(A(numbers('10.txt')))
    print(B(numbers('10.txt')))
