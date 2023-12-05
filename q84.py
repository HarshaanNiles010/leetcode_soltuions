from typing import List 

def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = []
    for i,j in enumerate(heights):
        start = i
        while stack and stack[-1][1] > j:
            idx, current_height = stack.pop()
            maxArea = max(maxArea, current_height * ( i - idx))
            start = idx
        stack.append((start,j))
    for i, j in stack:
        maxArea = max(maxArea, j * (len(heights) - i))
    return maxArea

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(heights))