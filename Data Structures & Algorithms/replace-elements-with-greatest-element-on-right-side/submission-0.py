class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans: List[int] = []

        for i in range(len(arr)):
            max: int = -1
            for j in range(i+1, len(arr)):
                if arr[j] > max:
                    max = arr[j]
            ans.append(max)
        
        return ans
            

