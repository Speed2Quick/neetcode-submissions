class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1

        while i < j and j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                j += 1
                continue
            while j < len(nums) - 1 and nums[i] == nums[j]:
                j += 1
            if nums[i] == nums[j]:
                break
            i += 1
            nums[i] = nums[j]
        return i + 1