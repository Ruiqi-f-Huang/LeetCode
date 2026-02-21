class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2
        path = []
        ans = []

        def dfs(i, left):
            if i == m:
                ans.append("".join(path)) # Concatenate the characters in the list into a string.
                return

            if left > i - left:
                path.append(')')
                dfs(i+1, left)
                path.pop()

            if left < n:
                path.append('(')
                dfs(i+1, left+1)
                path.pop()
        dfs(0, 0)
        return ans