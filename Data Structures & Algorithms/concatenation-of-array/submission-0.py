class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #create new array
        #place at current idx + length of original list

        ans: List[int] = [0] * (len(nums)*2)
        for i in range(0, len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans