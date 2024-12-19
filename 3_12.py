from collections import Counter

arr = [2, 3, 2, 5, 8, 1, 9, 8]
counter = Counter(arr)


uniq = [key for key, value in counter.items() if value == 1]

print(uniq)