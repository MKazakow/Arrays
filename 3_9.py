def compare(array1, array2):
    if len(array1) != len(array2): return False
    i = 0
    while i < len(array1):
        if array1[i] != array2[i]: return False
        i += 1
    return True

arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]

arr3 = [True, False]
arr4 = [True, False, True]

arr5 = [5, 3, 1]
arr6 = [5, 3, 1]

arr7 = [3, 2, 1]
arr8 = [3, 2]

print(f'Array1: {arr1}\nArray2: {arr2}\nArrays are the same: {compare(arr1, arr2)}')
print(f'Array1: {arr3}\nArray2: {arr4}\nArrays are the same: {compare(arr3, arr4)}')
print(f'Array1: {arr5}\nArray2: {arr6}\nArrays are the same: {compare(arr5, arr6)}')
print(f'Array1: {arr7}\nArray2: {arr8}\nArrays are the same: {compare(arr7, arr8)}')