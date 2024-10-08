from collections import deque
from typing import List


def calc_time(grid: List[List[int]]) -> int:
    q = deque()
    time, fresh = 0, 0
    rows = len(grid)
    columns = len(grid[0])
    # Traverse the grid and check where are the rotten and fresh oranges
    for row in range(rows):
        for column in range(columns):
            # If the orange is rotten store the coordinates
            if grid[row][column] == 2:
                q.append([row, column])
            # If the orange is fresh increment the fresh counter
            if grid[row][column] == 1:
                fresh += 1
    # use a neighbour matrix to check for the oranges in the vicinity
    neighbours = [[0,1],[0,-1],[-1,0],[1,0]]
    # run a multiple source BFS to check for time 
    while q and fresh > 0:
        for i in range(len(q)):
            i, j  = q.popleft()
            for coord_x, coord_y in neighbours:
                r = coord_x + i
                c = coord_y + j
                if (r < 0 or r == len(grid) or 
                    c < 0 or c == len(grid[0]) or
                    grid[r][c] != 1):
                    continue
                # Decrement the fresh oranges if orange is going to rot
                grid[r][c] = 2
                q.append([r,c])
                fresh -= 1
        time += 1
    # Return the time it took for oranges to rot otherwise return -1 indicating task is unsuccessful
    return time if fresh == 0 else -1


if __name__ == '__main__':
    grid = [[2,1,1], [1,1,0], [0,1,1]]
    t = calc_time(grid)
    print(t)
    new_grid = [[0,2]]
    t = calc_time(new_grid)
    print(t)