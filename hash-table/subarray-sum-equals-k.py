class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        s = ans = 0
        for x in nums:
            s += x
            cnt[s] += 1
            ans += cnt[s-k]
        return ans