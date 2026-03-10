class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        left_min = [0] * n
        right_max = [0] * n
        l = nums[0]
        r = nums[-1]

        for i in range(n):
            if nums[i] < l:
                left_min[i] = nums[i]
                l = nums[i]
            else:
                left_min[i] = l
        for i in range(n-1, -1, -1):
            if nums[i] > r:
                right_max[i] = nums[i]
                r = nums[i]
            else:
                right_max[i] = r

        for i in range(n):
            if nums[i] > left_min[i] and nums[i] < right_max[i]:
                return True
        return False
            
