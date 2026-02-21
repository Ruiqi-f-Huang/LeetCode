# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        even = False
        ans = []
        q = deque([root])

        while q:
            val = []
            for _ in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            ans.append(val[::-1] if even else val)
            even = not even
        
        return ans
