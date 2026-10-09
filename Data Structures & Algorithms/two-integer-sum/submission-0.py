class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        output = []
        for i in range(len(nums)):
            if target - nums[i] in count:
                output.append(count[target - nums[i]])
                output.append(i)
            else:
                count[nums[i]] = i
        return output
