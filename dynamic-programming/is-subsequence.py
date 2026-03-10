class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s0 = 0
        t0 = 0
        sn = len(s)
        tn = len(t)

        while s0 < sn:
            while t0 < tn and t[t0] != s[s0]:
                t0 += 1
            if t0 != tn:
                s0 += 1
            else:
                break
        return True if s0 == sn else False
