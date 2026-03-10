class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num = Counter(arr)
        freq = num.values()
        return True if len(freq) == len(set(freq)) else False