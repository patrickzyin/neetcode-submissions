class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #charCount to list of Anagrams

        for word in strs:
            count = [0] * 26 #a to z
            for c in word:
                count[ord(c) - ord("a")] += 1  #a = 80,  a-a = 0 , b-a= 1
            result[tuple(count)].append(word)
        return list(result.values())