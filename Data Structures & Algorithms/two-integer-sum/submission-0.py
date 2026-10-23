class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            remainder = target - nums[i]

            if remainder in values:
                return [min(values[remainder], i), max(values[remainder], i)]

            values[nums[i]] = i

    # target - current
    # find remainder

    # store current in hash table with val = remainder?
    # check if future val = remainder?