# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result_list = ListNode()
        result_head = result_list
        while l1 and l2:
            if l1.val < l2.val:
                result_list.next = l1
                l1 = l1.next
            else:
                result_list.next = l2
                l2 = l2.next
            result_list = result_list.next
        
        if l1:
            result_list.next=l1
        elif l2:
            result_list.next=l2

        return result_head.next
                