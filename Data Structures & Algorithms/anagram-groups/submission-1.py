class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        valid = defaultdict(list)

        for word in strs:
            valid["".join(sorted(word))].append(word)

        return list(valid.values())
