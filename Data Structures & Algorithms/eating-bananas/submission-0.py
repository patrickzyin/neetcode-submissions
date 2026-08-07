class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = R

        while L <= R:
            mid = (L+R) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours <= h:
                res = min(res,mid)
                R = mid - 1
            else:
                L = mid + 1
            
        return res