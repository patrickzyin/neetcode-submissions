class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        water = 0
        maxwater = 0
        while l < r:
            if heights[l] <= heights[r]:
                water = heights[l]*(r-l)
                maxwater = max(water,maxwater)
                l+=1
            elif heights[l] >= heights[r]:
                water = heights[r]*(r-l)
                maxwater = max(water,maxwater)
                r-=1
        return maxwater
        