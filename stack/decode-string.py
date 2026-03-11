class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(i):
            multi = 0
            res = ""
            while i < len(s):
                if s[i].isdigit():
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    tmp, i = dfs(i+1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return res, i
                else:
                    res += s[i]
                i += 1
            return res, i
        return dfs(0)[0]