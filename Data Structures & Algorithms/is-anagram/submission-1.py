class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = self.add_to_dict(s)
        t_count = self.add_to_dict(t)
        return s_count == t_count

    def add_to_dict(self, s: str):
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        return count
