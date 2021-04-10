# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root==None:
            return False
        if root.left==None and root.right==None:
            if root.val==targetSum:
                return True    

        l = self.hasPathSum(root.left, targetSum-root.val)
        r = self.hasPathSum(root.right, targetSum-root.val)

        return l or r
    
#         # DFS with stack
#         if not root:
#             return False
#         stack = [(root, root.val)]
#         while stack:
#             curr, val = stack.pop()
#             if not curr.left and not curr.right and val == sum:
#                 return True
#             if curr.right:
#                 stack.append((curr.right, val+curr.right.val))
#             if curr.left:
#                 stack.append((curr.left, val+curr.left.val))
#         return False
    
#         # BFS with queue
#         if not root:
#             return False
#         queue = [(root, sum-root.val)]
#         while queue:
#             curr, val = queue.pop(0)
#             if not curr.left and not curr.right and val == 0:
#                 return True
#             if curr.left:
#                 queue.append((curr.left, val-curr.left.val))
#             if curr.right:
#                 queue.append((curr.right, val-curr.right.val))
#         return False
    
    
    #recursive
#     if root==None:
#             return False
#         if root.left==None and root.right==None:
#             if root.val==targetSum:
#                 return True    

#         l = self.hasPathSum(root.left, targetSum-root.val)
#         r = self.hasPathSum(root.right, targetSum-root.val)

#         return l or r