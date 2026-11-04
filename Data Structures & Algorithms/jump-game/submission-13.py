class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_reachable = 0
        # 0, 2, 3 we start at 0, so we never update farthest_reachable because we should be able to just move it and do 
        for i in range(len(nums) - 1):
            if i > farthest_reachable:
                return False
            farthest_reachable = max(farthest_reachable, nums[i] + i)
            if farthest_reachable >= len(nums)-1:
                return True
        if len(nums) == 1:
            return True
        return False