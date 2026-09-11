class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()          # <-- 1. sort first
        res = []

        def backtrack(subset, index):
            res.append(subset.copy())    # <-- 2. append every time, not just at the end

            for i in range(index, len(nums)):     # <-- 3. loop over indices, starting from `index`
                if i > index and nums[i] == nums[i - 1]:   # <-- 4. skip duplicate values at this level
                    continue
                subset.append(nums[i])
                backtrack(subset, i + 1)          # <-- 5. move forward past i, not just index+1
                subset.pop()

        backtrack([], 0)
        return res