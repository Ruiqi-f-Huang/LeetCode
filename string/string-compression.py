class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = r = 0
        write = 0

        while r < n:
            while r < n and chars[r] == chars[l]:
                r += 1
            
            char = chars[l]
            num = r - l

            chars[write] = char
            write += 1
            if num != 1:
                for c in str(num):
                    chars[write] = c
                    write += 1
            
            l = r
        
        return write
