class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        suf = [1] * len(nums)
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]

        for i in range(len(nums)-2, -1, -1):
            suf[i] = nums[i+1] * suf[i+1]
            result[i] *= suf[i]
        
        return(result)
                