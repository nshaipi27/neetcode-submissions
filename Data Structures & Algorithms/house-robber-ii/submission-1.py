class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def helper(self, nums: List[int]) -> int:
            prev1, prev2 = 0, 0

            for num in nums:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr
            return prev1
        ans1, ans2 = helper(self, nums[1:]), helper(self,nums[:-1])
        return max(ans1, ans2)