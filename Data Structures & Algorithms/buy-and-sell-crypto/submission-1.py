class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        lowest = prices[0]
        for i in range(len(prices)):        
            lowest = min(lowest, prices[i])
            result = max(result, prices[i] - lowest)

        return result