from typing import List

def findUniquePath(obstacleGrid: List[List[int]]) -> int:
    ROWS = len(obstacleGrid)
    COLS = len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS - 1][COLS - 1] == 1: return 0
    dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
    dp[ROWS - 1][COLS - 1] = 1
    for row in range(ROWS - 1, -1, -1):
        for col in range(COLS - 1, -1, -1):
            if row == ROWS - 1 and col == COLS - 1: continue
            if obstacleGrid[row][col] == 1: dp[row][col] = 0
            else:
                dp[row][col] += dp[row + 1][col]
                dp[row][col] += dp[row][col + 1]
    return dp[0][0]

if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,0,0],[0,1,0]]
    print(findUniquePath(obstacleGrid))