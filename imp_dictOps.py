from mod_dictOps import (
    merge_dict, common_key, inv_dict, commonkey_pair
)

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 3, "d": 4}
dict3 = {"c": 3, "d": 4, "e": 5}


merged = merge_dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

common_keys = common_key(dict1, dict2, dict3)
print("Common Keys:", common_keys)


inverted_dict = inv_dict(dict1)
print("Inverted Dictionary:", inverted_dict)

common_pairs = commonkey_pair(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_pairs)
