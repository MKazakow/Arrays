def occurs(number, array):
    for i in array:
        if i == number: return True
    return False

arr = [15, 38, 7, 23, 14] 
nr = int(input("Podaj numer: "))
print(f"{nr} appears in the array: {occurs(nr, arr)}")