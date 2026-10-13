class Solution:
    def trap(self, height: List[int]) -> int:

        left = [0] * len(height)
        right = [0] * len(height)
        max_h = 0
        for i in range(len(height)):
            left[i] = max_h
            max_h = max(max_h, height[i])

        max_h = 0
        for i in range(len(height)-1, -1, -1):
            right[i] = max_h
            max_h = max(max_h, height[i])

        result = 0
        for i in range(len(height)):
            result += max(min(left[i], right[i]) - height[i], 0)
        
        return result
