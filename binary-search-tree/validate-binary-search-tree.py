# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self, node, left, right):
        if node is None:
            return True
        x = node.val
        return left < x < right and self.check(node.left, left, x) and self.check(node.right, x, right)
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.check(root, float('-inf'), float('inf'))
        