class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answers = []
        def dfs(i, curr_list): # i = 4, curr_list = [1, 2, 2, 4]
            if sum(curr_list) > target: # True
                return 
            if sum(curr_list) == target:
                answers.append(curr_list.copy())
                return 
            if i == len(candidates):
                return
            curr_list.append(candidates[i]) # curr_list = [1, 2, 2, 4]
            dfs(i + 1, curr_list) # Call dfs with index 3 and [1, 2, 2]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            curr_list.pop()
            dfs(i + 1, curr_list)
        dfs(0, [])
        return answers

            
