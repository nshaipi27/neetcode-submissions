class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest_reachable = 0
        min_jumps = 0
        current_boundary = 0

        for i in range(len(nums) - 1):
            farthest_reachable = max(farthest_reachable, nums[i] + i)
            if i == current_boundary:
                min_jumps += 1
                current_boundary = farthest_reachable
        return min_jumps            

