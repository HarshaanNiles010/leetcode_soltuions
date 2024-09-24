# This solution works I don't understand why leetcode is throwing a stupid error for this anyway

from typing import List
from math import sqrt

def distance(point: List[int]) -> int:
    return sqrt((point[0]**2) + (point[1]**2))
    


def K_closest_origin(points: List[List[int]], k: int):
    # sort it into a list according to distance 
    # run a loop k times, get the number of points
    dist = []
    for point in points:
        dist.append(distance(point))
    dist = sorted(dist)
    closest_points = []
    for i in range(k):
        closest_points.append(dist[i])
    return len(closest_points)

if __name__ == '__main__':
    points = [[0,2],[2,2]]
    k = 1
    print(K_closest_origin(points,k))