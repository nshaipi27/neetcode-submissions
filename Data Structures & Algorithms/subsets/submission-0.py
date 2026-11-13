class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        paths = []
        def dfs(i, curr_path):
            # We either include nums[i] or not include nums[i]
            
            if i == len(nums): # We are done
                return

            
            curr_path.append(nums[i])
            dfs(i + 1, curr_path)

            paths.append(curr_path.copy())
 
            curr_path.pop()
            dfs(i + 1, curr_path)

        dfs(0, [])
        paths.append([])
        return paths

            
            