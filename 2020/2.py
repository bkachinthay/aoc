from common import lines

def parse(line):
    rule, passwd = line.split(':')
    lmts, char = rule.split(' ')
    llmt, ulmt = [int(n) for n in lmts.split('-')]
    return (llmt, ulmt, char, passwd.strip())

def A(fname):
    valid_cnt = 0
    for l in lines(fname):
        llmt, ulmt, char, passwd = parse(l)
        cnt = passwd.count(char)
        if cnt >= llmt and cnt <= ulmt:
            valid_cnt += 1
    return valid_cnt

def B(fname):
    valid_cnt = 0
    for l in lines(fname):
        first, last, char, passwd = parse(l)
        if (passwd[first-1] != char and passwd[last-1] == char) or \
                (passwd[first-1] == char and passwd[last-1] != char):
            valid_cnt += 1
    return valid_cnt

if __name__ == "__main__":
    print(A('2a.txt'))
    print(B('2a.txt'))
