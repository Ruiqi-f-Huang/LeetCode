class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        for x in st:
            if x - 1 in st:
                continue
            i = 1
            while x + i in st:
                i += 1
            ans = max(ans, i)
        return ans