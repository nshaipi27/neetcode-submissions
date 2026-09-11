class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        classes = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            classes[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if classes[course] == []:
                return True
            visiting.add(course)

            for prereq in classes[course]:
                if  not  dfs(prereq):
                    return False
            visiting.remove(course)
            classes[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

        