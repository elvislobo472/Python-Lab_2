
from mod_setOps import (
    add_ele, remove_ele, union_intersect, diff, 
    is_subs, set_len, sym_diff, pow_set, uni_subset
)

set1 = {1, 2, 3, 4, 8, 10}
set2 = {3, 4, 5, 6, 19, 15}


print("Original Sets:")
print("Set1:", set1)
print("Set2:", set2)


add_ele(set1, 5)
print("\nAfter adding 5 to Set1:", set1)


remove_ele(set2, 6)
print("After removing 6 from Set2:", set2)

union, intersection = union_intersect(set1, set2)
print("\nUnion of Set1 and Set2:", union)
print("Intersection of Set1 and Set2:", intersection)

diff = diff(set1, set2)
print("\nDifference Set1 - Set2:", diff)


print("\nIs Set2 a subset of Set1?", is_subs(set2, set1))

print("\nLength of Set1 (without len()):", set_len(set1))


sym_diff = sym_diff(set1, set2)
print("\nSymmetric Difference of Set1 and Set2:", sym_diff)


power_set1 = pow_set(set1)
print("\nPower Set of Set1:", power_set1)

unique_subs = uni_subset(set1)
print("\nUnique Subsets of Set1:", unique_subs)
