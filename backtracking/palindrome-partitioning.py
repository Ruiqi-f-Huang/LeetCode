class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        ans = []
        path = []

        def isPalindrome(p):
            if p[::-1] == p:
                return True
            return False

        def dfs(i, start): # i: recursion times, start: substring start point
            if i == n:
                ans.append(path[:])
                return

            if i < n - 1:
                dfs(i+1, start)

            t = s[start: i+1]
            if isPalindrome(t):
                path.append(t)
                dfs(i+1, i+1)
                path.pop()
        dfs(0, 0)
        return ans
