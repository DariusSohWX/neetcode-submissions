class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += '@' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        start = 0
        while i < len(s):
            if s[i] == '@':
                length = int(s[start:i])
                start = i + 1 + length
                result.append(s[i+1:start])
                i = start
            i += 1

        return result