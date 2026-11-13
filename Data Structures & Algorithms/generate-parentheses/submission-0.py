class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(curr_path, opened, closed):
            if opened == n and closed == n:
                ans.append("".join(curr_path.copy()))
                return 
            
            if opened < n:
                curr_path.append('(')
                dfs(curr_path, opened + 1, closed)
                curr_path.pop()
            if closed < opened:
                curr_path.append(')')
                dfs(curr_path, opened, closed + 1)
                curr_path.pop()
            
        dfs([], 0, 0)
        return ans
