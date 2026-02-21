# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.getHeight(root) != -1

    def getHeight(self, node):
        if node is None:
            return 0
        l_height = self.getHeight(node.left)
        if l_height == -1:
            return -1
        r_height = self.getHeight(node.right)
        if r_height == -1 or abs(r_height - l_height) > 1:
            return -1
        return max(l_height, r_height) + 1