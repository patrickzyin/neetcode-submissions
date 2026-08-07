class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumIndex = {}  #val, index
        for i, n in enumerate(nums):
            complement = target - n
            if complement in sumIndex:
                return [sumIndex[complement], i]
            sumIndex[n] = i
