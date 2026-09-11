class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            print(sorted(s))
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        print(res.values())
        return list(res.values())
