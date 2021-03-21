import ast
import re
from common import lines

OPS = { '+', '*'}

def parse(s):
    return  re.findall('\S', s)

def apply(exp, a, b):
    return ((a * b) if exp == '*' else (a+b))

def isInt(n):
    return re.match('^\d+$', n)

def evala(exp):
    while len(exp) > 1:
        new_exp = []
        for i in range(3, len(exp) + 1):
            a, op, b = exp[i-3: i]
            if isInt(a) and op in OPS and isInt(b):
                new_exp.append(str(apply(op, int(a), int(b))))
                new_exp += exp[i:]
                break
            elif a == '(' and b == ')':
                new_exp.append(op)
                new_exp += exp[i:]
                break
            else:
                new_exp.append(a)
        exp = new_exp
    return exp[0]

def evalb(exp):
    if len(exp) == 1:
        return exp[0]
    itr = 0
    for ei, e in enumerate(exp):
        if e == '(':
            itr += 1
        elif e == ')':
            itr -= 1
        elif e == '*' and itr == 0:
            return str(apply(e, int(evalb(exp[:ei])), int(evalb(exp[ei+1:]))))
    op, opi = '', -1
    for ei, e in enumerate(exp):
        if e == '(':
            itr += 1
        elif e == ')':
            itr -= 1
        elif e == '+' and itr == 0:
            op = e
            opi = ei
            break
    if opi == -1:
        return evalb(exp[1:-1])
    return str(apply(op, int(evalb(exp[:opi])), int(evalb(exp[opi+1:]))))

def A(lns):
    return sum(int(evala(parse(l))) for l in lns)

def B(lns):
    return sum(int(evalb(parse(l))) for l in lns)

s1 = "2 * 3 + (4 * 5)"
s2 = "5 + (8 * 3 + 9 + 3 * 4 * 3)" 
s3 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))" 
s4 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2" 
assert evala(parse(s1)) == '26'
assert evala(parse(s2)) == '437'
assert evala(parse(s3)) == '12240'
assert evala(parse(s4)) == '13632'
assert evalb(parse(s1)) == '46'
assert evalb(parse(s2)) == '1445'
assert evalb(parse(s3)) == '669060'
assert evalb(parse(s4)) == '23340'

def parse_expr(line) -> tuple: 
    "Parse an expression: '2 + 3 * 4' => (2, '+', 3, '*', 4)."
    return ast.literal_eval(re.sub('([+*])', r",'\1',", line))

if __name__ == '__main__':
    print('herel', A(lines('18.txt')))
    print('herel', B(lines('18.txt')))
    print('--- norvig parse ---- ')
    print(parse_expr(s1))
    print(parse_expr(s2))
    print(parse_expr(s3))
    print(parse_expr(s4))
