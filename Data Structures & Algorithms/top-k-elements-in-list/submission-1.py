class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times_appeared = defaultdict(int)

        for num in nums:
            times_appeared[num] += 1
        
        ans = list(dict(sorted(times_appeared.items(),
          key=lambda value: value[1],
          reverse=True)))

        return ans[:k]
        
