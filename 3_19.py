arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = int(input("Podaj liczbe: "))
count = 0
for i in arr:
    if i > val: count += 1

print(arr)
print(f"There are {count} numbers greater then {val} in array")