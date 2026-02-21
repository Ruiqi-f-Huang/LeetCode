class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = []
        ans = []
        on_path = [False] * n
        m = 2 * n - 1
        diag1 = [False] * m
        diag2 = [False] * m

        def dfs(r):
            if r == n:
                ans.append(['.'* l + 'Q' + '.'* (n-l-1) for l in col])
                return
            for c in range(n):
                if on_path[c] == False and diag1[r+c] == False and diag2[r-c] == False:
                    col.append(c)
                    on_path[c] = diag1[r+c] = diag2[r-c] = True
                    dfs(r+1)
                    col.pop()
                    on_path[c] = diag1[r+c] = diag2[r-c] = False
                    
        dfs(0)
        return ans
