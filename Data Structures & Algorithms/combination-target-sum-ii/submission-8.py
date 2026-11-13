class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        ans = []

        def dfs(i, curr_path, curr_sum): 
            if curr_sum == target: 
                ans.append(curr_path.copy())
                return
            if curr_sum > target: 
                return 
            if i == len(candidates):
                return 
            
            curr_path.append(candidates[i]) 
            curr_sum += candidates[i] 
            dfs(i + 1, curr_path, curr_sum) 
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 
            v = curr_path.pop() 
            curr_sum -= v 
            dfs(i + 1, curr_path, curr_sum)
        dfs(0, [], 0)
        return ans
            