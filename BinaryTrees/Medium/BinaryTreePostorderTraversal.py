# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #flipped condition(my own logic)
        vals = []
        stack = []
        prev = None
        curr = root

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack[len(stack)-1]
                if curr.right and curr.right!=prev:
                    curr = curr.right
                else:
                    stack.pop()
                    vals.append(curr.val)
                    prev=curr
                    curr=None
        return vals
    
    
#         #iterative l r n
#         result = []
#         stack = []
#         cur = root
#         prev = None
        
#         while cur or stack:
#             if cur:
#                 stack.append(cur)
#                 cur = cur.left
#             else:
#                 cur=stack[len(stack)-1]
#                 if not cur.right or cur.right==prev:
#                     result.append(cur.val)
#                     stack.pop()
#                     prev = cur
#                     cur = None
#                 else:
#                     cur=cur.right
#         return result
        
        #recursive
        # result = []
        # if root:
        #     result.extend(self.postorderTraversal(root.left))
        #     result.extend(self.postorderTraversal(root.right))
        #     result.append(root.val)
        # return result
            