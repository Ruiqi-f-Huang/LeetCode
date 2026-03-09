class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        n = len(candies)
        ans = [False] * n
        for i, x in enumerate(candies):
            if x + extraCandies >= m:
                ans[i] = True
        return ans

        