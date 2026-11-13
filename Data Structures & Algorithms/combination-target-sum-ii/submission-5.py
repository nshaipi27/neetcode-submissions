class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answers = []
        def dfs(i, curr_list, curr_sum): 
            if curr_sum > target: 
                return 
            if curr_sum == target:
                answers.append(curr_list.copy())
                return 
            if i == len(candidates):
                return
            curr_list.append(candidates[i])
            curr_sum = sum(curr_list)
            dfs(i + 1, curr_list, curr_sum) 
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            v = curr_list.pop()
            curr_sum -= v
            dfs(i + 1, curr_list, curr_sum)
        dfs(0, [], 0)
        return answers

            
