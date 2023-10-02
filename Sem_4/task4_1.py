# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):

    new_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
   
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
        
    return new_matrix

current_matrix = [[1, 2, 3],      # 1 4 7
                  [4, 5, 6],      # 2 5 8
                  [7, 8, 9]]      # 3 6 9

print(transpose_matrix(current_matrix))