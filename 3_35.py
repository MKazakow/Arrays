def transpose_matrix(m):
    matrix = []
    try:
        matrix = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    except(TypeError) as e:
        for i in m:
            matrix.append([i])
    # for i in range(len(m)):
    #     for j in range(len(m[0])):
    #         matrix[j][i] = m[i][j]

    return matrix

m1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m2 = [
    [1,2,3,4,5],
    [6,7,8,9,0]
]
m3 = [5,6,7,8]

m4 = [
    [1],
    [2],
    [3]
]

print(transpose_matrix(m1))
print(transpose_matrix(m2))
print(transpose_matrix(m3))
print(transpose_matrix(m4))
