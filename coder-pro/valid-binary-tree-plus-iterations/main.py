class Node(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def inOrderRecTraversal(self, root):
    if root:
      # First recur on left child
      self.inOrderRecTraversal(root.left)
      # then print the data of node
      print(root.val),
      # now recur on right child
      self.inOrderRecTraversal(root.right)
    return
  
  def postOrderRecTraversal(self, root):
    if root:
      self.postOrderRecTraversal(root.left)
      self.postOrderRecTraversal(root.right)
      print(root.val)
    return 

  def preOrderRecTraversal(self, root):
    if root:
      print(root.val)
      self.preOrderRecTraversal(root.left)
      self.preOrderRecTraversal(root.right)
    return 

  def inOrderTraversalStack(self, root):
    flag = True
    if root:
      stack = []
      while flag:
        while root is not None:
          stack.append(root)
          root = root.left
        if len(stack)==0:
          flag=False
          break
        node = stack.pop()
        root = node.right
        print(node.val)
    return

  def preOrderTraversalQueue(self, root):
    flag = True
    if root:
      stack = []
      while flag:
        while root is not None:
          stack.append(root)
          root = root.left
        if len(stack)==0:
          flag=False
          break
        node = stack.pop(0)
        root = node.right
        print(node.val)
    return

  #first print children left to right, then root / parent
  def postOrderTraversalStack(self, root):
    stack = []
    prev = None
    if not root:
      return
    while root or len(stack)!=0:
      if root is not None:
        stack.append(root)
        if root.left:
          root = root.left
        else:
          root = None
        # print(root)
      else:
        root = stack[-1] #stack[-1] --- peek 
        if root.right and root.right!=prev:
          root = root.right
        else:
          stack.pop()
          print(root.val)    
          prev = root
          root = None
        # if not root.right or root.right==prev:
        #   stack.pop()
        #   print(root.val)    
        #   prev = root
        #   root = None
        # else:
        #   root = root.right
    return

  def _isBSTValidHelper(self, n, left, right):
    left_subtr = True
    right_subtr = True
    if n == None: 
        return True
    if left:
        left_subtr = self._isBSTValidHelper(left, left.left, left.right) and n.val > left.val
    # else:
    #     left_subtr = True
    if right:
        right_subtr = self._isBSTValidHelper(right, right.left, right.right) and n.val < right.val
    # else:
    #     right_subtr = True
    return left_subtr and right_subtr

  def isBSTValid(self, n):
    return self._isBSTValidHelper(n, n.left, n.right)

#   5
#  / \
# 4   7
#    / \
#   6   8
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.right = Node(8)
node.right.left = Node(6)
print(Solution().isBSTValid(node)) #true

#   5
#  / \
# 4   7
#    / \
#   6   4
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.right = Node(4)
node.right.left = Node(6)
print(Solution().isBSTValid(node)) #false
#Solution().inOrderTraversalStack(node)

  #    6
  #   / \
  #  4   7
  # / \   \
  #2   6   4
node = Node(6)
node.left = Node(4)
node.right = Node(7)
node.right.right = Node(4)
node.left.right = Node(6)
node.left.left = Node(2)
print(Solution().isBSTValid(node)) #false
Solution().postOrderTraversalStack(node)
