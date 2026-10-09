class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count1 = {}
        count2 = {}
        for a in s:
            count1[a] = count1.get(a, 0) + 1
        for a in t:
            count2[a] = count2.get(a, 0) + 1

        return count1 == count2
