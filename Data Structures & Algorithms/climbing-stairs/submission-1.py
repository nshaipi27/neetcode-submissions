class Solution:
    def climbStairs(self, n: int) -> int:
        ans = []

        for i in range(n):
            if i == 0:
                ans.append(1)
            elif i == 1:
                ans.append(2)
            else:
                ans.append(ans[i-1] + ans[i-2])
        return ans[-1]