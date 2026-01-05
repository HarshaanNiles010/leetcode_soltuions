from typing import List
from collections import deque
def findShortestPath(grid: List[List[int]]):
    ROWS = len(grid)
    COLS = len(grid[0])
    queue = deque()
    visit = set()
    queue.append((0,0)) # Starting index
    visit.add((0,0)) # visited the starting point
    length = 0

    while queue:
        qLen = len(queue)
        for i in range(qLen):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1: return length
            nei = [[0,-1], [0,1], [1,0],[-1,0]]
            for dr, dc in nei:
                if min(r, c) < 0 or r + dr == ROWS or c + dc == COLS or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1: continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1
    return -1

if __name__ == '__main__':
    grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
    ]
    
