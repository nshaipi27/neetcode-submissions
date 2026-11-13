class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, curr_path, curr_sum): # 2, [2, 5, 6], 13
            if curr_sum == target:
                ans.append(curr_path.copy())
                return
            if curr_sum > target: # we're here, so we return
                return                 
            if i == len(nums):
                return 
            # we can include the current number again, or skip it
            curr_path.append(nums[i])
            curr_sum += nums[i]
            dfs(i, curr_path, curr_sum)

            # skip current number
            curr_path.pop()
            curr_sum -= nums[i]
            dfs(i + 1, curr_path, curr_sum)

        dfs(0, [], 0)
        return ans