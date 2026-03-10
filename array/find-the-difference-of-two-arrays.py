class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        ans = [[], []]
        
        for x in s1:
            if x not in s2:
                ans[0].append(x)
        
        for x in s2:
            if x not in s1:
                ans[1].append(x)

        return ans