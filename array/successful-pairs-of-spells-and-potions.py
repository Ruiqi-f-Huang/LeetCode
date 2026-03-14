class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def find(products: List[int], success: int) -> int:
            n = len(products)
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if products[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            return n - left

        ans  = [] * len(spells)
        potions = sorted(potions)
        for x in spells:
            target = success
            target = target / x
            num = find(potions, target)
            ans.append(num)
        return ans