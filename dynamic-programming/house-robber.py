class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        ## Step 1: Backtracking - time limiting
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     return max(dfs(i-1), dfs(i-2)+nums[i])
        
        # ans = dfs(n-1)
        # return ans

        ## Step 2: memo - space limiting
        # cache = [-1] * n
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]
            
        #     ans = max(dfs(i-1), dfs(i-2)+nums[i])
        #     cache[i] = ans
        #     return ans
       
        # return dfs(n-1)

        ## Step 3: recursion - space limiting
        # f = [0] * (n+2)
        # for i, x in enumerate(nums):
        #     f[i+2] = max(f[i+1], f[i]+x)

        # return f[n+1]

        ## Step 4: recursion with space optimization
        f0 = f1 = 0 # f1: last state, f0: last last state
        for i, x in enumerate(nums):
            newF = max(f1, f0 + x)
            f0 = f1
            f1 = newF
        return f1


        