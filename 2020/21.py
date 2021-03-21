from re import sub
from common import flatten, read

s = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

def parse_line(l):
    first, second = sub('\)|contains|\,', '', l).split('(')
    return [first.strip().split(), second.strip().split()]

def parse(s):
    return [parse_line(l) for l in s.split('\n')]

def possible_allerggens(parsed):
    allergen_names = {}
    for ingredients, allergens in parsed:
        for allergen in allergens:
            if allergen not in allergen_names:
                allergen_names[allergen] = []
            allergen_names[allergen].append(set(ingredients))
    possble_allergen_names = {}
    for allergen, ingredients in allergen_names.items():
        possble_allergen_names[allergen] = set.intersection(*ingredients)
    return possble_allergen_names

def possible_names(s):
    parsed = parse(s)
    all_ingredients = flatten([ings for ings, allerg in parsed])
    ingredient_set = set(all_ingredients)
    possble_allergen_names = possible_allerggens(parsed)
    allergen_set = set.union(*possble_allergen_names.values())
    non_allergens = ingredient_set - allergen_set
    return sum(all_ingredients.count(allrg) for allrg in non_allergens)

def mapped_allergens(parsed):
    possible_allergen_names = possible_allerggens(parsed)
    mapped = {}
    allergen_keys = set(possible_allergen_names.keys())
    while allergen_keys:
        for allergen in allergen_keys.copy():
            unidentified = list(filter(lambda ingr: ingr not in mapped.values(), possible_allergen_names[allergen]))
            if len(unidentified) == 1:
                mapped[allergen] = unidentified[0]
                allergen_keys.remove(allergen)
    return ','.join([ing for _, ing in sorted(mapped.items())])

inp = read('21.txt').strip()

print(possible_names(s))
print('---')
print(possible_names(inp))

print('--- part b --- ')
print(mapped_allergens(parse(s)))
print('---')
print(mapped_allergens(parse(inp)))

