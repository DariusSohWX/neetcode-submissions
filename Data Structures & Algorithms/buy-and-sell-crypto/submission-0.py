class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        lowest = 0
        for i in range(len(prices)):
            if i == 0:
                lowest = prices[i]
            
            lowest = min(lowest, prices[i])
            result = max(result, prices[i] - lowest)

        return result