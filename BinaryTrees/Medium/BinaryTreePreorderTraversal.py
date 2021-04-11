# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #iterative using stack
        stack=[]
        result=[]
        if root:
            stack.append(root)
            while stack:
                node = stack.pop()
                result.append(node.val)
                
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result
        
        
        
    #     result=[]
    # #recursive solution
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     result=[]
    #     if root:
    #         result.append(root.val)
    #         if root.left:
    #             result.extend(self.preorderTraversal(root.left))
    #         if root.right:
    #             result.extend(self.preorderTraversal(root.right))
    #     return result
            