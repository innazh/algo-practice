# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #recursive
        res = self.isMirror(root.left,root.right)
        return res
        
    def isMirror(self,root:TreeNode, root2:TreeNode)->bool:
        if root==None and root2==None:
            return True
        if root==None or root2==None:
            return False
        res = self.isMirror(root.left, root2.right) and self.isMirror(root.right,root2.left)
        res2 = root.val==root2.val
        return res and res2
        
        
        #iterative
        # q = []
        # q.append(root)
        # q.append(root)
        # while q:
        #     n1 = q.pop()
        #     n2 = q.pop()
        #     if n1==None and n2==None:
        #         continue
        #     if n1==None or n2==None:
        #         return False
        #     if n1.val!=n2.val:
        #         return False
        #     q.append(n1.left)
        #     q.append(n2.right)
        #     q.append(n1.right)
        #     q.append(n2.left)
        # return True
            