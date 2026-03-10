class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        nums.sort() # cannnot write nums = nums.sort()
        l = 0
        r = n - 1

        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                ans += 1
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else: 
                r -= 1
        return ans