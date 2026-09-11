class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def helper(self, nums: List[int]) -> int:
            if len(nums) == 1: return nums[0]

            prev2, prev1 = 0, 0

            for n in nums:
                curr = max(prev1, prev2 + n)
                prev2 = prev1
                prev1 = curr
            return prev1

        return max(helper(self, nums[1:]), helper(self, nums[:-1]))