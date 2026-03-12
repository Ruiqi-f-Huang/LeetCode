# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(Node: Optimal[TreeNode], cnt, left:bool):
            if Node is None:
                return 0
            cnt += 1
            nonlocal ans
            ans = max(ans, cnt)

            if left:
                dfs(Node.right, cnt, False)
                dfs(Node.left, 0, True)
            else:
                dfs(Node.left, cnt, True)
                dfs(Node.right, 0, False)
        left = dfs(root.left, 0, True)
        right = dfs(root.right, 0, False)
        return ans
            