class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowels(ch):
            if ch.lower() in 'aeiou':
                return True
            else:
                return False

        n = len(s)
        s = list(s)
        l = 0
        r = n - 1
        while l < r:
            while l < r and is_vowels(s[l]) == False:
                l += 1
            while l < r and is_vowels(s[r]) == False:
                r -= 1

            s[r], s[l] = s[l], s[r]
            l += 1
            r -= 1

        return "".join(s)
