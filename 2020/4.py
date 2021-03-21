from common import read
import re

FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]


def valid_byr(v):
    return bool(re.match('^\d+$', v) and 1920 <= int(v) <= 2002)

def valid_iyr(v):
    return bool(re.match('^\d+$', v) and 2010 <= int(v) <= 2020)

def valid_eyr(v):
    return bool(re.match('^\d+$', v) and 2020 <= int(v) <= 2030)

def valid_hgt(v):
    m = re.match('^(\d+)(cm|in)$',v)
    if not m:
        return False
    n = int(m.group(1))
    return bool(( m.group(2) == 'cm' and (150 <= n <= 193) ) or \
            ( m.group(2) == 'in' and (59 <= n <= 76) ))

def valid_hcl(v):
    return bool(re.match('^#[a-f0-9]{6}$', v))

def valid_ecl(v):
    return bool(re.match('^amb|blu|brn|gry|grn|hzl|oth$', v))

def valid_pid(v):
    return bool(re.match('^[0-9]{9}$', v))

FIELD_VALIDATE = [
    valid_byr,
    valid_iyr,
    valid_eyr,
    valid_hgt,
    valid_hcl,
    valid_ecl,
    valid_pid
]

FIELD_MAP = {k: fn for (k,fn) in zip(FIELDS, FIELD_VALIDATE)}

def valid_b(k, v):
    return k == 'cid' or k in FIELDS and FIELD_MAP[k](v)

def passports(fname):
    return read(fname).split('\n\n')

def fields(s):
    return [f.split(':') for f in re.findall(r'\S+', s)]

def fkeys(arr):
    return [f[0] for f in arr]

def vals(arr):
    return [f[1] for f in arr]

def is_valid(pport):
    return all([f in fkeys(fields(pport)) for f in FIELDS])

def is_validb(pport):
    return all([valid_b(k,v) for (k,v) in fields(pport)])

def A(fname):
    return sum(is_valid(pport) for pport in passports(fname))

def B(fname):
    return sum(is_valid(pport) and is_validb(pport)\
            for pport in passports(fname))

assert bool(valid_byr('2002')) == True
assert bool(valid_byr('2003')) == False
assert bool(valid_hgt('60in')) == True
assert bool(valid_hgt('190cm')) == True
assert bool(valid_hgt('190in')) == False
assert bool(valid_hgt('190')) == False
assert bool(valid_hcl('#123abc')) == True
assert bool(valid_hcl('#123abz')) == False
assert bool(valid_hcl('123abc')) == False
assert bool(valid_ecl('brn')) == True
assert bool(valid_ecl('wat')) == False
assert bool(valid_pid('000000001')) == True
assert bool(valid_pid('0123456789')) == False

valid_str = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

invalid_str = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

assert sum([is_validb(pport) for pport in valid_str.split('\n\n')]) == 4
assert sum([is_validb(pport) for pport in invalid_str.split('\n\n')]) == 0

if __name__ == "__main__":
    print(A('4a.txt'))
    print(B('4a.txt'))
