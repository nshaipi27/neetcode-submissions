class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        numComponents = 0
        for edge, neighbor in edges:
            adj_list[edge].append(neighbor)
            adj_list[neighbor].append(edge)
        
        visited = set()
        def dfs(node):
            nonlocal numComponents
            if node in visited:
                return
            visited.add(node)
            
            for neighbor in adj_list[node]:
                dfs(neighbor)


        for i in range(n):
            if i not in visited:
                dfs(i)
                numComponents += 1

        return numComponents
        
