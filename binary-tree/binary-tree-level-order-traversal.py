# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        q = deque([root])

        while q:
            val = []
            for _ in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(val)
        return ans

        