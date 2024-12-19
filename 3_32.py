arr = [[1, 8, 4, 0, 10],
       [60, 50, 40, 50, 100],
       [5, 5, 5, 5, 5],
      ]

print("Tablica:")
print (arr)
       
arr[0], arr[2] = arr[2], arr[0]

print("Tablica po zamianie:")
print(arr)