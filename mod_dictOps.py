from collections import defaultdict

def merge_dict(*args):
    merged = {}
    for d in args:
        if not isinstance(d, dict):
            raise TypeError("All arguments must be dictionaries.")
        merged.update(d)
    return merged

def common_key(*args):
    if not args:
        return set()
    
    common_keys = set(args[0].keys())
    for d in args[1:]:
        if not isinstance(d, dict):
            raise TypeError("All arguments must be dictionaries.")
        common_keys &= set(d.keys())
    
    return common_keys

def inv_dict(d):
    inverted = defaultdict(list)
    
    for key, value in d.items():
        inverted[value].append(key)
    
    return dict(inverted)

def commonkey_pair(*args):
    if not args:
        return set()
    
    common_pairs = set((k, v) for k, v in args[0].items())
    for d in args[1:]:
        if not isinstance(d, dict):
            raise TypeError("All arguments must be dictionaries.")
        common_pairs &= set((k, v) for k, v in d.items())
    
    return common_pairs



