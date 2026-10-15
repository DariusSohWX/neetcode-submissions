class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq_s1 = {}
        freq_s2 = {}
        for c in s1:
            freq_s1[c] = freq_s1.get(c, 0) + 1
        print(freq_s1)

        i, j = 0, 0
        while j < len(s2) and i <= j:

            while j < len(s2) and j-i+1 <= len(s1):
                freq_s2[s2[j]] = freq_s2.get(s2[j], 0) + 1
                j += 1
             

            print(freq_s2)
            if freq_s1 == freq_s2:
                return True
            
            freq_s2[s2[i]] -= 1
            if freq_s2[s2[i]] == 0:
                del freq_s2[s2[i]]

            i += 1

        return False