class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)
        n = len(gain)
        for i in range(1, n):
            gain[i] = gain[i-1] + gain[i]
        return max(gain)