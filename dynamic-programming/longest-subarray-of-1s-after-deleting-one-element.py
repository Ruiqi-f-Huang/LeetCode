class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        cnt0 = 0
        for right, x in enumerate(nums):
            if x == 0: cnt0 += 1
            while cnt0 > 1:
                if nums[left] == 0: cnt0 -= 1
                left += 1
            ans = max(ans, right-left)
        return ans
        