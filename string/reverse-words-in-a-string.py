class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ans = []
        n = len(s)
        l = r = n - 1
        while l >= 0 and r >= 0:
            while l >= 0 and s[l] != ' ':
                l -= 1
            ans.append(s[l+1: r+1]) # [)
            l = l - 1
            while l >= 0 and s[l] == ' ':
                l -= 1
            r = l
        return ' '.join(ans)
        
        