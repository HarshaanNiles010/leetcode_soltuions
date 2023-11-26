from typing import List

def newOrder(matrix: List[List[int]]) -> List[int]:
    # Take 4 pointers and revolve them around the matrix to solve the question
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)
    res = []
    while left < right and top < bottom:
        # For the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # for the right most column
        for j in range(top, bottom):
            res.append(matrix[j][right - 1])
        right -= 1
        if not ( left < right and top < bottom):
            break
        # for the bottom row
        for k in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][k])
        bottom -= 1
        # for the left column
        for l in range(bottom - 1, top - 1, -1):
            res.append(matrix[l][left])
        left += 1
    return res

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(newOrder(matrix))