class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r, result = 0, len(heights) - 1, 0
        while l < r:
            left = heights[l]
            right = heights[r]
            area = (r-l) * min(left, right)
            result = max(area, result)
            if left <= right:
                l += 1
            elif left > right:
                r -= 1

        return result
