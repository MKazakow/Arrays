arr = [[-38, 19], [5,40],[-7,11],[29,16]]
smallest = [0, 0, 0]
largest = [0, 0, 0]

for i in arr:
    for j in i:
        if j < smallest[0]: smallest[0] = j; smallest[1] = (arr.index(i)); smallest[2] = (i.index(j))
        elif j > largest[0]: largest[0] = j; largest[1] = (arr.index(i)); largest[2] = (i.index(j))

#print(smallest)
#print(largest)

print(f"Largest number is {largest[0]} and is located in row {largest[1]+1} and column {largest[2]+1}")
print(f"Smallest number is {smallest[0]} and is located in row {smallest[1]+1} and column {smallest[2]+1}")