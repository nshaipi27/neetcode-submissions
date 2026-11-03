class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        # -4, -1, -1, 0, 1, 2
        for i in range(len(nums) - 2): # nums[i] = -4
            l, r = i + 1, len(nums) - 1 # nums[l] = -1, nums[r] = 1
            print(l, r)
            while l < r: # i = 1, r = 4
                if nums[i] + nums[l] + nums[r] > 0: # the sum is -4
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1 # l = 3
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        ans = []
        for (a, b, c) in res:
            ans.append([a, b, c])
        return ans

