import random

def rand_elem(arr):

    return random.choice(arr)

arr = [1,2,3,4,5,6,7,8,9]

for i in range(7):  
    print(rand_elem(arr), end=" ")