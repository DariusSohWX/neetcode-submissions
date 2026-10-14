class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        seen = set()
        result = 0
        curr = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] in seen:
                while i < j and s[i] != s[j]:
                    seen.discard(s[i])
                    curr -= 1
                    i += 1

                curr -= 1
                i += 1

            curr += 1
            result = max(result, curr)
            seen.add(s[j])
            j += 1

        return result