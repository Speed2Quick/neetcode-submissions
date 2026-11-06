class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        product, zero_count = 1, 0

        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return res

        for i, c in enumerate(nums):
            if zero_count: res[i] = 0 if c else product
            else: res[i] = product // c

        return res
            