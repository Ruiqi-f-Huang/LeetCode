class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[i0], nums[i] = nums[i], nums[i0]
                i0 += 1
                