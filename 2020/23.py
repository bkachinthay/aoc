from time import time
from common import mapl

s = '389125467'

def decr(num, min_num, max_num, exclude):
    new_num = max_num if (num - 1) < min_num else (num - 1)
    return decr(new_num, min_num, max_num, exclude)\
        if new_num in exclude else new_num

def part1(s, it=10):
    cups = mapl(int, s)
    min_val = min(cups)
    max_val = max(cups)

    for _ in range(it):
       curr_cup = cups.pop(0)
       picked_cups, rest = cups[:3],\
               cups[3:] + [curr_cup]
       dest_cup = decr(curr_cup, min_val, max_val, picked_cups)
       # print(dest_cup) 
       insert_idx = rest.index(dest_cup) + 1
       cups = rest[:insert_idx] + picked_cups + rest[insert_idx:]
    index_1 = cups.index(1)
    return ''.join(mapl(str, cups[index_1+1:] + cups[:index_1]))

def stringify(start, cups):
    i = start
    s =  ''
    for _ in (cups.keys()):
        s += ', ' + str(i)
        i = cups[i]
    return s

# efficient version of part1
def part2(cups, it=10):
    next_cup = {}
    max_val, min_val  = 0, float('Infinity')
    prev_val= cups[-1]
    for c in cups:
        if max_val < c:
            max_val = c
        if min_val > c:
            min_val = c
        next_cup[prev_val] = c
        prev_val = c
    curr_cup = cups[0]
    for i in range(it):
        chosen = [next_cup[curr_cup],\
                next_cup[next_cup[curr_cup]],\
                next_cup[next_cup[next_cup[curr_cup]]]]
        move_to = decr(curr_cup, min_val, max_val, chosen)
        next_cup[curr_cup] = next_cup[chosen[2]]
        next_cup[chosen[2]] = next_cup[move_to]
        next_cup[move_to] = chosen[0]
        curr_cup = next_cup[curr_cup]
    # return stringify(1, next_cup).replace(', ', '')[1:]
    return  next_cup[1] * next_cup[next_cup[1]]

inp = '962713854'

# print(part1(s, 100))

t = time()
print(part2(mapl(int, inp) + list(range(10, 1000001)), 10000000))
print('time : ', time() - t)
print('------------------')
