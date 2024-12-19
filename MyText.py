def wordsCount(x):
    return len(x.split())

def longToShort(x):
    arr = x.split()
    arr = sorted(arr, key=len, reverse=True)
    return arr

def alphabetical(x):
    arr = x.split()
    arr.sort()
    return arr
