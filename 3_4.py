#min max 

def largest(arr, n):
 

    max = arr[0]
 

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
 
 

arr = [-15, 8, -31, 47, -2, 19]
n = len(arr)
Ans = largest(arr, n)
print( Ans)