class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        left_max = 0
        right_max = 0
        max_right_vals = [0] * len(height)

        for i in range(len(height)-1, 0, -1):
            right_max = max(height[i], right_max)
            max_right_vals[i] = right_max
        
        for i in range(len(height) - 1):
            left_max = max(left_max, height[i]) # 0
            shorter_boundary = min(left_max, max_right_vals[i])

            if shorter_boundary - height[i] > 0:
                trapped_water += shorter_boundary - height[i]
        
        return trapped_water