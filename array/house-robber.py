class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i-1), dfs(i-2)+nums[i])
        
        ans = dfs(n-1)
        return ans
        