class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLength = 0
        L = 0
       
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[r])
            maxLength = max(maxLength, r - L + 1)

        return maxLength