class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        len_s = len(s)
        if len_s == 0:
            return 0
        elif len_s == 1:
            return 1

        result, l = 0, 0
        freq = {}

        for r in range(len_s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            sub_len = r - l + 1
            req_k = sub_len - max(freq.values())
            while req_k > k:
                freq[s[l]] -= 1
                l += 1
                sub_len -= 1
                req_k = sub_len - max(freq.values())
            
            result = max(result, sub_len)

        return result