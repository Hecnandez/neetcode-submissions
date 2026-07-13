class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        islands = 0

        def dfs(i):
            if i in visit: return
            visit.add(i)

            for j in adj[i]:
                dfs(j)

        for i in range(n):
            if not i in visit: 
                dfs(i)
                islands += 1
        
        return islands
