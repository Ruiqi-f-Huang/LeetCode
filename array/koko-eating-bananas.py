class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            t = 0
            mid = (left + right) // 2
            for x in piles:
                t += (x + mid - 1) // mid
            if t <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left