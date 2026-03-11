# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        ans = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        while slow:
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt

        cur1 = head
        cur2 = pre
        while cur2:
            ans = max(ans, cur1.val+cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next
        return ans

        