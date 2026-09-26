class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we use a sliding window of length s1 to iterate through s2 and check whether this window in s2 is a permutation 
    
        def isPermutation(s1, s2):
            freq1 = {}
            freq2 = {}
            for s in s1:
                freq1[s] = freq1.get(s, 0) + 1
            for s in s2:
                freq2[s] = freq2.get(s, 0) + 1
            return freq1 == freq2
        window = len(s1)
        count = 0
        while count < len(s2):
            print(s2[count:count+window])
            if isPermutation(s1,s2[count:count+window]):
                return True
            count += 1
        return False
