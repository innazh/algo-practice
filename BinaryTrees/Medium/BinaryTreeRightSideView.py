# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        queue = deque()
        result = []
        
        if root:
            queue.append(root)
        
        while queue:
            rightNode = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    rightNode = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightNode:
                result.append(rightNode.val)
        return result