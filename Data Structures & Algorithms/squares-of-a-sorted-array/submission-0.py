class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                answer.appendleft(nums[l] * nums[l])
                l += 1
            else:
                answer.appendleft(nums[r] * nums[r])
                r -= 1
        return list(answer)