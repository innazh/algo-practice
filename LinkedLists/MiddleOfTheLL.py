import math

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None:
            return head

        LL_len = 1
        curr_node = head
        hash_set = {}
        hash_set[LL_len-1]= curr_node
        while curr_node.next:
            LL_len+=1
            curr_node = curr_node.next
            hash_set[LL_len-1]=curr_node
        
        middle_idx = math.ceil((LL_len-1)/2)
        if LL_len % 2 != 0:
            return hash_set[int(middle_idx)]
        return hash_set[middle_idx+1]
    

# first try lmao....
        