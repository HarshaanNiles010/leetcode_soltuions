from typing import List

def  path_count(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(grid: List[List[int]], r: int, c: int, visit: set) -> int:
        if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1:
            return 0
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        visit.add((r, c))

        count = 0
        count += dfs(grid, r + 1, c, visit)
        count += dfs(grid, r - 1, c, visit)
        count += dfs(grid, r, c + 1, visit)
        count += dfs(grid, r, c - 1, visit)

        visit.remove((r,c))
        return count
    return dfs(grid,0,0,set())

# Driver
if __name__ == '__main__':
    grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
    ]