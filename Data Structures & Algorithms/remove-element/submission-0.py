class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int = 0
        
        for i in range(0, len(nums)):
            if nums[i] != val:
                k += 1
            elif nums[i] == val:
                j: int = i
                while j < len(nums):
                    if nums[j] == val and j == len(nums)-1:
                        return k
                    elif nums[j] == val:
                        j += 1
                        continue
                    nums[i] = nums[j]
                    nums[j] = val
                    k += 1
                    break
        return k

# any value that is not == val needs to be swapped
# increment k for every non == val that is found