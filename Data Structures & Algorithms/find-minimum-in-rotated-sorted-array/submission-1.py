class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        res = nums[0]

        while L <= R:
            if nums[L] < nums[R]:
                res = min(res,nums[L])
                break
            mid = (L + R) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[L]:  #if everything left is already sorted, search everything right
                L = mid + 1
            else:    #everything right is sorted, search everything left
                R = mid 
        return res