class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        cnt0 = 0

        for right, x in enumerate(nums):
            if x == 0: cnt0 += 1
            while cnt0 > k:
                if nums[left] == 0: cnt0 -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans