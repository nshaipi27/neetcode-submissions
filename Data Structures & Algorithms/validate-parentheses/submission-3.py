class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in matches:
                if not stack or stack[-1] != matches[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
        
        