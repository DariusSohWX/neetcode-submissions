class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        seen = set()
        result = 0

        for num in nums_set:

            if num in seen:
                continue

            length = 1

            # go backwards
            i = num - 1
            while i in nums_set and not (i in seen):
                seen.add(i)
                length += 1
                i -= 1


            # go forward
            i = num + 1
            while i in nums_set and not (i in seen):
                seen.add(i)
                length += 1
                i += 1

            result = max(result, length)

        return result