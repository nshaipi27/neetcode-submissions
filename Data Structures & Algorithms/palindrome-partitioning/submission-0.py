class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        def dfs(i, curr_path):
            if i == len(s):
                ans.append((curr_path.copy()))
            for j in range(i, len(s)):
                piece = s[i:j + 1]
                if piece == piece[::-1]:
                    curr_path.append(piece)
                    dfs(j + 1, curr_path)
                    curr_path.pop()
            
        dfs(0, [])
        return ans