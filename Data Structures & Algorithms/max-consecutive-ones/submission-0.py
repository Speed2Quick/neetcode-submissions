class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans: int = 0
        current_sum: int = 0
        for num in nums:
            if num:
                current_sum += 1
            else:
                ans = max(ans, current_sum)
                current_sum = 0
        return max(ans, current_sum)