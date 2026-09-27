class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        freq_s1 = {}
        freq_s2 = {} 
        window, count = len(s1), 0 

        for i in range(len(s1)):
            freq_s1[s1[i]] = freq_s1.get(s1[i], 0) + 1
            freq_s2[s2[i]] = freq_s2.get(s2[i], 0) + 1

        if freq_s1 == freq_s2:
            return True
        
        while count + window < len(s2):
            if freq_s1 == freq_s2:
                return True
            else:
                freq_s2[s2[count]] =freq_s2.get(s2[count], 0) - 1
                if freq_s2[s2[count]] == 0:
                    del freq_s2[s2[count]]
                count += 1
                freq_s2[s2[count + window - 1]] = freq_s2.get(s2[count + window - 1], 0) + 1
                if freq_s1 == freq_s2:return True

        return False
        
