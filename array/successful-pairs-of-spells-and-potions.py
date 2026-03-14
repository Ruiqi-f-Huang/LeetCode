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
        for x in spells:
            products = [x * y for y in potions]
            products = sorted(products)
            num = find(products, success)
            ans.append(num)
        return ans