arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]
sumaostatniej = 0

for i in arr:
    sumaostatniej += i[-1]

print("Suma wartości w ostatniej kolumnie:", sumaostatniej)