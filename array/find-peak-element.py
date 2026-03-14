class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 2
        while left <= right:
            m = (left + right) // 2
            if nums[m] < nums[m+1]:
                left = m + 1
            else: 
                right = m - 1
        return left