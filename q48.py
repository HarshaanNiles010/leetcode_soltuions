from typing import List

def rotate(matrix: List[List[int]]) -> None:
    length = len(matrix)
    breadth = len(matrix[0])
    #print(f"{length} => length and {breadth} => breadth")
    matrix = matrix[::-1]
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
    print(matrix)

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)