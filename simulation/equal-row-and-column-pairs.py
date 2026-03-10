class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        row = Counter(tuple(row) for row in grid)
        col = zip(*grid)
        for x in col:
            ans += row[x]
        return ans
