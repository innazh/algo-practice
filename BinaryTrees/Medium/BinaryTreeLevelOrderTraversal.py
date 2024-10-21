# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        #using queue
        queue = []
        queue.append(root)
        
        while queue:
            nodesNum = len(queue)#how many nodes are on the current level
            currentLvl = []#contains the nodes on the current level
            for i in range(nodesNum):
                node = queue.pop(0)
                currentLvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(currentLvl)
        return result
    
    
        # can also use deque:
        #     queue = deque()
        # result = []

        # if root:
        #     queue.append(root)

        # while queue:
        #     curr_list = []
        #     for i in range(len(queue)):
        #         curr = queue.popleft()
        #         curr_list.append(curr.val)
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     result.append(curr_list)
        # return result