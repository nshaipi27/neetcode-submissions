class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop_max(nums))
        return ans[-1]