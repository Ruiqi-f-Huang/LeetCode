# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafValues(self, node: Optional[TreeNode]):
        ans = []
        def dfs(root: Optinal[TreeNode]):
            if root == None:
                return
            if root.left == None and root.right == None:
                ans.append(root.val)
            
            dfs(root.left)
            dfs(root.right)
        dfs(node)
        return ans

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = self.leafValues(root1)
        leaf2 = self.leafValues(root2)
        return True if leaf1 == leaf2 else False
        