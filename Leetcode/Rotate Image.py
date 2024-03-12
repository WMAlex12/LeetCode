

def rotate(matrix):
    n = len(matrix)
    for i in range(n): 
        for j in range(i): 
            matrix[i][j], matrix[j][i]  = matrix[j][i], matrix[i][j]
    # for i in matrix: 
    #     print(i)
    #     i.reverse()
    print(matrix)    
    
matrix = [[1,2,3], [4,5,6],[7,8,9]]
rotate(matrix)