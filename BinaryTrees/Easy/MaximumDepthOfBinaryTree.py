# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #iterative
        if root==None:
            return 0
        q = []
        q.append(root)
        depth=0
        while q:
            depth+=1
            nodesOnLvl = len(q)
            for i in range(nodesOnLvl):
                itm = q.pop(0)
                if itm.right:
                    q.append(itm.right)
                if itm.left:
                    q.append(itm.left)

        return depth
        # recursive
        # if not root:
        #     return 0
        # l = self.maxDepth(root.left)
        # r = self.maxDepth(root.right)
        # return 1+max(l,r)