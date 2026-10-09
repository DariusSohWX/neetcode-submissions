class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            result[tuple(count)].append(s)

        return list(result.values())
    
