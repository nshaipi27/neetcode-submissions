class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        paths = []
        def dfs(i, curr_path):
           
            if i == len(nums):
                paths.append(curr_path.copy())

                return
            

            curr_path.append(nums[i])
            dfs(i + 1, curr_path)

            while i +1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            curr_path.pop()
            dfs(i+1 , curr_path)
        dfs(0, [])
        return paths
            