def convert(m):
    array = []
    for i in m:
        for j in i:
            array.append(j)
    return array

m1 = [
    [2, 3],
    [1, 5]
]

m2 = [
    [5,0,3,7,5],
    [9,0,9,1,2]
]

m3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

print(convert(m1))
print(convert(m2))
print(convert(m3))