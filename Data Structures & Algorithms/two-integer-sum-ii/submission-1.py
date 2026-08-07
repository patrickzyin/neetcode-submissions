class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1
        res = []
        while L < R:
            if numbers[L] + numbers[R] > target:
                R-=1
            elif numbers[L] + numbers[R] < target:
                L+=1
            elif numbers[L] != numbers[R] and numbers[L] + numbers[R] == target:
                res = [L+1,R+1]
                return res