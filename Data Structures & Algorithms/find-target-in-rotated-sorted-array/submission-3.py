class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid

            if nums[L] <= nums[mid]: #search right
                if target > nums[mid] or target < nums[L]:
                    L = mid + 1
                else:
                    R = mid - 1
            else:   #search left
                if target < nums[mid] or target > nums[R]:
                    R = mid - 1
                else:
                    L = mid + 1
        return -1