# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = slow.next
        return head
        