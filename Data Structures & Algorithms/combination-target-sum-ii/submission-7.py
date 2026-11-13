class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # 1, 2, 2, 4, 5, 6, 9 
        ans = []

        def dfs(i, curr_path, curr_sum): # 4, [1, 2, 2, 4], 9
            if curr_sum == target: 
                print(curr_sum, curr_path)

                ans.append(curr_path.copy())
                return
            if curr_sum > target: # true 
                return 
            if i == len(candidates):
                return 
            
            # We can include the current number, or skip it
            # inclusion case
            curr_path.append(candidates[i]) # [1, 2, 2, 4]
            curr_sum += candidates[i] # sum = 9
            dfs(i + 1, curr_path, curr_sum) # i = 3, [1, 2, 2, 4], 9
            
            # Skip this number
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 # this will take us to 4
            v = curr_path.pop() # 1, 2, 2
            curr_sum -= v # sum = 5
            dfs(i + 1, curr_path, curr_sum)
        dfs(0, [], 0)
        return ans
            