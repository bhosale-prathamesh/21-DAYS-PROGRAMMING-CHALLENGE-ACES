class Node:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.val = key

root = Node(1)
'''
    1
   / \
None None
'''
root.left = Node(2)
root.right = Node(3)
'''
* - None
        1
      /   \ 
     2     3
    / \   / \
   *   * *   *
'''
root.left.right = Node(4)
'''
* - None
            1
         /    \
        2      3
       / \    / \
      *   4  *   *
         / \
        *   *
'''
