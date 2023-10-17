from typing import List


def findMedian(nums1: List[int], nums2: List[int]):
    if not nums1:
        left = 0
        right = len(nums2)
        if len(nums2) % 2 == 0:
            mid = int((left + right) // 2)
            median = (nums2[mid - 1] + nums2[mid]) / 2
            return float(median)
        else:
            mid = int((left + right) // 2)
            median = nums2[mid]
            return float(nums2[mid])
    elif not nums2:
        left = 0
        right = len(nums1)
        if len(nums1) % 2 == 0:
            mid = int((left + right) // 2)
            median = (nums1[mid - 1] + nums1[mid]) / 2
            return float(median)
        else:
            mid = int((left + right) // 2)
            median = nums1[mid]
            return float(nums1[mid])
    else:
        nums = nums1 + nums2
        nums.sort()
        left = 0
        right = len(nums)
        if len(nums) % 2 == 0:
            mid = int((left + right) // 2)
            median = (nums[mid - 1] + nums[mid]) / 2
            return float(median)
        else:
            mid = int((left + right) // 2)
            median = nums[mid]
            return float(nums[mid])            

if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = []
    print(findMedian(nums1,nums2))