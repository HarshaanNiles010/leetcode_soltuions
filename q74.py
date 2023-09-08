from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left)//2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1



def searchMatrix(nums: List[List[int]], target: int) -> int:
    for i,j in enumerate(nums):
        if target > j[0] and target < j[len(j) - 1]:
            if binarySearch(j,target) != -1:
                return True
    return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(searchMatrix(matrix,target))