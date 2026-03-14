class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st = set(nums)
        ans = 1
        for x in st:
            if x - 1 not in st:
                continue
            i = 1
            while x + i in st:
                i += 1
            ans = max(ans, i+1)
        return ans