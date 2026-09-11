class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[r] > prices[l]:
                curr_profit = prices[r] - prices[l]
                profit = max(profit, curr_profit)
            else:
                l = r
            r += 1
        return profit
        