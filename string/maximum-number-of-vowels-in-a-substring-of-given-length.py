class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        max_v = 0
        v = 0

        for i, x in enumerate(s):
            if x in 'aeiou':
                v += 1
            if i < k - 1:
                continue
            max_v = max(max_v, v)
            if s[i-k+1] in 'aeiou':
                v -= 1
        
        return max_v