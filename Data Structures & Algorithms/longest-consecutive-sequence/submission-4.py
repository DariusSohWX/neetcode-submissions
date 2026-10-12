class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        result = 0

        for num in nums_set:

            if num - 1 in nums_set:
                continue

            # go forward
            length = 1
            i = num + 1
            while i in nums_set:
                length += 1
                i += 1

            result = max(result, length)

        return result