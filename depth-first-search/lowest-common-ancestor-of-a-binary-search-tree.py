# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        x = root.val
        if p.val > x and q.val > x:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < x and q.val < x:
            return self.lowestCommonAncestor(root.left, p, q)
        return root