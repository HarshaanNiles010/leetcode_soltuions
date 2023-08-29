from typing import List
def total_rain_water(height:List[int]) -> int:
    # we are given a list containg heihgt of the column at ith position the width of the column is always one
    # using the two pointer approach 
    l = 0
    r = len(height) - 1
    #get the height at the left most point
    leftHieght = height[l]
    # get the height at the right most point
    rightHeight = height[r]
    # store the total area of water in another variable and keep adding to it
    result = 0
    while l < r:
        # now since the area is width * height but the width is always the same i.e 1
        # so the rain water trapped will become the height difference between the two pillars 
        if leftHieght < rightHeight:
            l += 1
            # here just check if the height on the current pointer is greater than or less than the previous
            leftHieght = max(leftHieght,height[l])
            result += leftHieght - height[l]
        else:
            r -= 1
            rightHeight = max(rightHeight,height[r])
            # here just check if the height on the current pointer is greater than or less than the previous
            result += rightHeight - height[r]
    return result

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(total_rain_water(height))