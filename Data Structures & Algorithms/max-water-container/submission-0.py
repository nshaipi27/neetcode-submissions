class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            h1, h2 = heights[l], heights[r]
            curr_height = min(h1, h2)
            curr_width = (r - l)
            curr_vol = curr_height * curr_width
            res = max(res, curr_vol)

            if h1 < h2:
                l += 1
            else:
                r -= 1
        return res
            
            
