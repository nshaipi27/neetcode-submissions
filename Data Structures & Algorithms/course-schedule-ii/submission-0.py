class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        path = []

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        visited = set()
        def dfs(node, curr_path):
            if node in curr_path:
                return False
            if node in visited:
                return True

            curr_path.append(node)
            for prereq in adj_list[node]:
                if not dfs(prereq, curr_path):
                    return False
            visited.add(node)
            path.append(node)
            curr_path.pop()
            return True
    
        for i in range((numCourses)):
            if i in adj_list:
                if not dfs(i, []):
                    return []
            else:
                path.append(i)
        return path
            
        
                
            