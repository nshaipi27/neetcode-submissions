class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = 0
        ans = float('inf')

        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[-1], cost[-2])
