class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        def dfs(u, v, visited): # u is the current node, v is the target node 
            if u == v:
                return True
        
            visited.add(u)

            for edge in adj[u]:
                if edge in visited:
                    continue
                if dfs(edge, v, visited):
                    return True
            return False

        for u, v in edges:
            if dfs(u, v, set()):
                return [u, v]
            adj[u].append(v)
            adj[v].append(u)
        