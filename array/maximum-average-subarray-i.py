class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        l = 0
        r = k - 1
        s = 0

        while r < n:
            s = max(s, sum(nums[l: r+1]))
            r += 1
            l += 1
            
        return s / k
        