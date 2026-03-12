# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        cur = [root]
        LevelSum = []
        while cur:
            ls = 0
            next = []
            for x in cur:
                ls += x.val
                if x.left: next.append(x.left)
                if x.right: next.append(x.right)
            LevelSum.append(ls)
            cur = next
        return LevelSum.index(max(LevelSum)) + 1