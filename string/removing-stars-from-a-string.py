class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for x in s:
            if x != '*':
                st.append(x)
            else:
                st.pop()
        return "".join(st)