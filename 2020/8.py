from common import lines

def walk(instructions):
    visited, curr, acc = set(), 0, 0
    while curr not in visited:
        # print('walk : ', visited, acc, curr)
        visited.add(curr)
        act, val = instructions[curr].split(' ')
        if act == 'jmp':
            curr += int(val)
        elif act == 'acc':
            acc += int(val)
            curr += 1
        else:
            curr += 1
        if curr == len(instructions):
            return acc, 'term'
    return acc, 'loop'

def A(lines):
    return walk(lines)[0]

def B(lines):
    for l, li in zip(lines, range(len(lines))):
        if l[:3] == 'jmp' or l[:3] == 'nop':
            newl = l.replace('jmp', 'nop') if 'jmp' in l else l.replace('nop', 'jmp')
            val, cond = walk(lines[:li] + [newl] + lines[li+1:])
            if cond == 'term':
                return val

s1 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".strip().split('\n')

assert walk(s1) == (5, 'loop')
assert B(s1) == 8

if __name__ == '__main__':
    print('start')
    print(A(lines('8.txt')))
    print(B(lines('8.txt')))
    print('done')
