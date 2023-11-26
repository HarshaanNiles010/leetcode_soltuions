from typing import List

def setZeroes(matrix: List[List[int]]):
    length = len(matrix)
    breadth = len(matrix[0])
    rowZero = False

        
    for i in range(length):
        for j in range(breadth):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                if i > 0:
                    matrix[i][0] = 0
                else:
                    rowZero = True

    for i in range(1, length):
        for j in range(1, breadth):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(length):
            matrix[i][0] = 0

    if rowZero:
        for j in range(breadth):
            matrix[0][j] = 0

if __name__ == '__main__':
    #matrix = [[1,1,1],[1,0,1],[1,1,1]]
    #print(setZeroes(matrix))
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(setZeroes(matrix))