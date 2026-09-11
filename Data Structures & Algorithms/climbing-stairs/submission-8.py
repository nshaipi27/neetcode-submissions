class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        prev1, prev2 = 2, 1
        for _ in range(3,n+1):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr
            print("prev2:", prev2)
            print("prev1:",prev1)
        return prev1