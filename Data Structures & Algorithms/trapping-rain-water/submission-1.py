class Solution:
    def trap(self, height: List[int]) -> int:

        left = [0] * len(height)
        max_h = 0
        for i in range(len(height)):
            left[i] = max_h
            max_h = max(max_h, height[i])

        max_h = 0
        result = 0
        for i in range(len(height)-1, -1, -1):
            result += max(min(left[i], max_h) - height[i], 0)
            max_h = max(max_h, height[i])
        
        return result
