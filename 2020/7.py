from re import subn
from common import read

def getMap(lst):
    bags = {}
    for l in lst.strip().split('\n'):
        line, _ = subn('bags?|\.|\s', '', l)
        bag, content = line.split('contain')
        bags[bag] = {} if content == 'noother' else\
                { b[1:]: b[0] for b in content.split(',')} 
    return bags

def A(lst, bag_color):
    bags = getMap(lst)
    all_possible = set()
    frontier = [bag_color]
    while frontier:
        new_frontier = []
        for f in frontier:
            for bag, content in bags.items():
                if f in content:
                    new_frontier.append(bag)
        all_possible = all_possible.union(new_frontier)
        frontier = new_frontier
    return len(all_possible)

def B(lst, bag_color):
    bags = getMap(lst)
    bags_contained = 0
    frontier = [(bag_color, 1)]
    while frontier:
        new_frontier = []
        f, cf = frontier.pop()
        content = bags[f]
        if content:
            for bag, bc in content.items():
                frontier.append((bag, int(bc) * cf))
                bags_contained += int(bc) * cf
    return bags_contained

s1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

s2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

assert A(s1, 'shinygold') == 4
assert B(s2, 'shinygold') == 126

if __name__ == '__main__':
    print(A(read('7.txt'), 'shinygold'))
    print(B(read('7.txt'), 'shinygold'))
