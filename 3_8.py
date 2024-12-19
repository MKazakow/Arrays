arr = [2,6,4,9,7]


def star (arr):
    for i in arr:
        print(i, end=": ")
        for j in range(i):
           print("*", end="")
        print()
       
    return arr


print (star(arr))