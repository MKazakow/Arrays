

def second_largest(arr):
    arr_sorted = sorted(arr)
    return arr_sorted[-2]

def range_diff(arr):
    return max(arr) - min(arr)

def median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    
    if n % 2 == 1:
        return arr_sorted[n // 2]
    else:
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2

def min_max(arr):
    return [min(arr), max(arr)]

def numbers_as_string(arr):
    return "-".join(str(x) for x in arr)
