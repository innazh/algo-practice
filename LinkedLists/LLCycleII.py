# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow,fast = head,head
        while fast and fast.next:
            fast=fast.next.next
            slow = slow.next
            if slow==fast:
                break

        if not fast or not fast.next:
            return None
        
        s2=head
        while s2!=slow:
            slow=slow.next
            s2=s2.next
        return s2