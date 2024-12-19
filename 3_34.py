
def identity_matrix(rozmiar):
    matrix = [[0] * rozmiar for _ in range(rozmiar)]
    
    for i in range(rozmiar):
        matrix[i][i] = 1
        
    return matrix

def print_matrix(matrix):
    for i in matrix:
        print(" ".join(map(str, i)))

for rozmiar in [3, 5, 8]:
    print(f"Macierz jednostkowa o wymiarze {rozmiar}x{rozmiar}:")
    a = identity_matrix(rozmiar)
    print_matrix(a)
