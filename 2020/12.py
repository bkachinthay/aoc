from common import lines

directions = {
    'E': {'L90': 'N', 'L180': 'W', 'L270': 'S', 'L360': 'E', 'R90': 'S', 'R180': 'W', 'R270': 'N', 'R360': 'E'},
    'N': {'L90': 'W', 'L180': 'S', 'L270': 'E', 'L360': 'N', 'R90': 'E', 'R180': 'S', 'R270': 'W', 'R360': 'N'},
    'W': {'L90': 'S', 'L180': 'E', 'L270': 'N', 'L360': 'W', 'R90': 'N', 'R180': 'E', 'R270': 'S', 'R360': 'W'},
    'S': {'L90': 'E', 'L180': 'N', 'L270': 'W', 'L360': 'S', 'R90': 'W', 'R180': 'N', 'R270': 'E', 'R360': 'S'}
}

def move(pos, instr):
    (direction, (x, y)) = pos
    if instr[0] in ['L', 'R']:
        return (directions[direction][instr], (x, y))
    move_dir, move_val = instr[0], int(instr[1:])
    if move_dir == 'F':
        move_dir = direction

    if move_dir == 'N':
        return (direction, (x, y+move_val))
    elif move_dir == 'S':
        return (direction, (x, y-move_val))
    elif move_dir == 'E':
        return (direction, (x+move_val, y))
    elif move_dir == 'W':
        return (direction, (x-move_val, y))

directionsB = {
        'R90': { 'E': 'N', 'S': 'E', 'W': 'S', 'N': 'W'},
        'R180': { 'E': 'W', 'S': 'N', 'W': 'E', 'N': 'S'},
        'R270': { 'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'},
        'R360': { 'E': 'E', 'S': 'S', 'W': 'W', 'N': 'N'},
        'L90': { 'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'},
        'L180': { 'E': 'W', 'S': 'N', 'W': 'E', 'N': 'S'},
        'L270': { 'E': 'N', 'S': 'E', 'W': 'S', 'N': 'W'},
        'L360': { 'E': 'E', 'S': 'S', 'W': 'W', 'N': 'N'}
}

def moveB(waypos, shippos, instr):
    if instr[0] in ['L', 'R']:
        dirs = directionsB[instr]
        return {
            'E': waypos[dirs['E']],
            'N': waypos[dirs['N']],
            'S': waypos[dirs['S']],
            'W': waypos[dirs['W']]
        }, shippos
    move_dir, move_val = instr[0], int(instr[1:])
    if move_dir == 'F':
        return waypos, (shippos[0] + (waypos['E'] - waypos['W']) * move_val, shippos[1] + (waypos['N'] - waypos['S']) * move_val)

    return {k: (v+move_val if move_dir == k else v) for k,v in waypos.items()}, shippos

def A(instructions):
    pos = ('E', (0,0))
    for instr in instructions:
        pos = move(pos, instr)
    # print(pos)
    (direction, (x, y)) = pos
    return abs(x) + abs(y)

def B(instructions):
    waypos = { 'E': 10, 'N': 1, 'W': 0, 'S': 0}
    shippos = (0,0)
    for instr in instructions:
        waypos, shippos = moveB(waypos, shippos, instr)
    # print('B : ', waypos, shippos)
    return sum(map(abs, shippos))

s1 = """F10
N3
F7
R90
F11""".strip().split('\n')
assert A(s1) == 25
assert B(s1) == 286

if __name__ == '__main__':
    print(A(lines('12.txt')))
    print(B(lines('12.txt')))
