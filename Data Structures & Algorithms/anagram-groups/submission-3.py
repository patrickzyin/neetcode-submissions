class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            result[sortedWord].append(word)
        return list(result.values())
            