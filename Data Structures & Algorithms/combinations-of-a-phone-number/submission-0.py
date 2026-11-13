class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {
            '1' : [],
            '2' : ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': []
        }
        ans = []
        nums = list(digits)
        def dfs(i, curr_path):
            if i == len(nums):
                ans.append("".join(curr_path.copy()))
                return
            for letter in mapping[nums[i]]:
                curr_path.append(letter)
                dfs(i + 1, curr_path)
                curr_path.pop()
        
        dfs(0, [])
        return ans
            