from itertools import chain, combinations

def add_ele(s, elem):
    s.add(elem)

def remove_ele(s, elem):
    s.discard(elem)

def union_intersect(s1, s2):
    u = s1 | s2
    intersect = s1 & s2
    return u, intersect

def diff(s1, s2):
    return s1 - s2

def is_subs(s1, s2):
   return s1.issubset(s2)

def set_len(s):
    count = 0
    for _ in s:
        count += 1
    return count

def sym_diff(s1, s2):
    return s1 ^ s2

def pow_set(s):
    pow_set_res = set()
    for subset in chain.from_iterable(combinations(s, r) for r in range(len(s)+1)):
        pow_set_res.add(frozenset(subset))
    return pow_set_res

def uni_subset(s):
    return pow_set(s)
