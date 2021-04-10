# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative
        stack = []
        result = []
        cur = root
            
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                result.append(cur.val)
                cur=cur.right
        return result
            
        # #recursive
        # result=[]
        # if root:
        #     result.extend(self.inorderTraversal(root.left))
        #     result.append(root.val)
        #     result.extend(self.inorderTraversal(root.right))
        # return result