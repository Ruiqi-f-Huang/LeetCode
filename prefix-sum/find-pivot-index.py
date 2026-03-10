class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_s = 0
        for i, x in enumerate(nums):
            if 2 * left_s == s - x:
                return i
            left_s += x
        return -1