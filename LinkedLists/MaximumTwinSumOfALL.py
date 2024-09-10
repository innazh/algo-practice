# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# A bit of a crazy attempt... O(n) time and O(1) space though.
# It seems like the code can be a bit simpler had I reversed the left half but this one is easier to understand I think
class Solution(object):
    def reverseLL(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow,fast = head, head
        end_first_half=None
        while fast:
            end_first_half=slow
            slow = slow.next
            fast = fast.next.next
        
        second_half_reversed = self.reverseLL(slow)
        end_first_half.next = second_half_reversed

        max_twin_sum = float("-inf")
        curr = head

        while curr and second_half_reversed:
            curr_twin_sum = curr.val + second_half_reversed.val
            max_twin_sum = max(max_twin_sum, curr_twin_sum) 
            curr = curr.next
            second_half_reversed = second_half_reversed.next
        return max_twin_sum