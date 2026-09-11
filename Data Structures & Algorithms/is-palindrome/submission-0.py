class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        q = deque((re.sub(r'[^a-zA-Z0-9]', '', s)).lower())
        
        while len(q) > 1:
            if q[0] == q[-1]:
                q.popleft()
                q.pop()
            else:
                return False
        
        return True