class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]
        for i, node in edges:
            graph[i].append(node)
            graph[node].append(i)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                if not dfs(neighbor, node):
                    return False
                
            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n


        