from typing import List
import heapq
def findPrimTree(n: int, edges: List[List[int]]) -> int:
    adj = {}
    for i in range(n):
        adj[i] = []
    for n1, n2, weight in edges:
        adj[n1].append([n2, weight])
        adj[n2].append([n1, weight])
    minHeap = [[0,0]]
    res = 0
    visit = set()
    while minHeap and len(visit) < n:
        weight, v = heapq.heappop(minHeap)
        if v in visit: continue
        res += weight
        visit.add(v)
        for nei, weight in adj[v]:
            if nei not in visit:
                heapq.heappush(minHeap, [weight, nei])
    return res if len(visit) == n else -1