# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return head

        dummy = ListNode(next = head)
        cur  = dummy
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                # while cur.next.next and cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

        