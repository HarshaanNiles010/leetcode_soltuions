from typing import List
from collections import deque


def find_islands(grid: List[List[int]]):
    if not grid:
        return 0
    
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    island_count = 0
    
    
    def bfs(r,c):
        q = deque()
        visited.add((r,c))
        q.append((r,c))
        
        while q:
            i, j = q.popleft()
            # neighbours abv as n
            n = [[0,1],[0,-1],[1,0],[-1,0]]
            for coord_x, coord_y in n:
                r = coord_x + i
                c = coord_y + j
                if ((r) in range(rows) and
                    (c) in range(columns) and
                    grid[r][c] == "1" and
                    (r, c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))
    
    for row in range(rows):
        for column in range(columns):
            #Check to see if the current position is land, if it is store it's coordinates
            if grid[row][column] == "1" and (row,column) not in visited:
                bfs(row,column)
                island_count += 1
    return island_count






if __name__ == '__main__':
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    print(find_islands(grid))
    new_grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    print(find_islands(new_grid))