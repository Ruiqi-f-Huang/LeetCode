# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSame(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSame(p.left, q.right) and self.isSame(p.right, q.left)
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isSame(root.left, root.right)
        