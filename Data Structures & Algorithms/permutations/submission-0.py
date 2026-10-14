class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        path = []
        def dfs():
            if len(path) == len(nums):
                permutations.append(path.copy())
                return
            
            for n in nums:
                if n in path:
                    continue
                path.append(n)
                dfs()
                path.pop()
        
        dfs()
        return permutations
