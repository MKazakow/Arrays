tuple1 = (50, 20, 40, 50, 30, 50)
value = int(input("Podaj szukaną liczbę: "))
count = 0
for i in tuple1:
    if i == value: count += 1

print("Number of occurances: ", count)