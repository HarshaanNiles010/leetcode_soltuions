from typing import List
from collections import deque

def find_max_area(grid: List[List[int]]):
    if not grid:
        return 0
    
    # Get the number of rows
    rows = len(grid)
    # Get the number of columns
    columns = len(grid[0])
    # set the visited set
    visited = set()
    
    def dfs(r,c):
        if (
            r < 0 or
            r == rows or
            c < 0 or 
            c == columns or
            grid[r][c] == 0 or
            (r,c) in visited
        ):
            return 0
        visited.add((r,c))
        return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1) 
    
    area = 0
    for row in range(rows):
        for column in range(columns):
            area = max(area, dfs(row,column))
    return area



if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(find_max_area(grid))