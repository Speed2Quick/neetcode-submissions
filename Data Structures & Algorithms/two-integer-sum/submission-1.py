class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            remainder = target - nums[i]

            if remainder in values:
                return [values[remainder], i]

            values[nums[i]] = i