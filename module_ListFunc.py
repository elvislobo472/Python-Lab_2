def max_1(x):
    if not x:
        raise ValueError("The list is empty.")
    return max(x)


def min_1(x):
    if not x:
        raise ValueError("The list is empty.")
    return min(x)


def calc_sum(x):
    if not x:
        return 0
    return sum(x)

def comp_avg(x):
    if not x:
        raise ValueError("The list is empty.")
    return calc_sum(x) / len(x)

def med(x):
    if not x:
        raise ValueError("The list is empty.")
    
    sort_list = sorted(x)
    n = len(sort_list)
    mid = n // 2
    
    if n % 2 == 0:
        return (sort_list[mid - 1] + sort_list[mid]) / 2
    else:
        return sort_list[mid]
