from typing import List
from collections import defaultdict
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        topSort = []
        visited = set()  # Visited nodes
        visiting = set() # Nodes being visited in the current DFS call (used to detect cycles)
        
        def dfs(src: int) -> bool:
            if src in visited:
                return True
            if src in visiting:
                return False  # A cycle is detected

            visiting.add(src)
            
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False  # A cycle is detected
                
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)
            
            return True  # No cycle detected

        for i in range(n):
            if not dfs(i):
                return []  # Return an empty list if a cycle is detected
        
        topSort.reverse()
        return topSort

if __name__ == "__main__":
    solution = Solution()
    edges = [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]
    n = 6
    print(solution.topologicalSort(n, edges))  # Output could be [5,4,2,3,1,0] or [4,5,2,3,1,0] etc.