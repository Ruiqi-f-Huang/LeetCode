class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        last = 0
        for x in asteroids:
            if x > 0:
                ans.append(x)
            else:
                while ans and ans[-1] <= -x:
                    last = ans[-1]
                    ans.pop()
                if not ans and last + x != 0:
                    ans.append(x)
        return ans