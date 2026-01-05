# Problem: Insert into a BST

# Pattern: Binary Search Logic.

# Why: We simulate searching for the value. When we hit a None (null) pointer, that's exactly where the new node belongs to maintain the sorted property.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def insertIntoBST(root, val):
  if not root:
    return TreeNode(val)

  if val < root.val:
    root.left = insertIntoBST(root.left, val)
  else:
    root.right = insertIntoBST(root.right, val)

  return root

# Complexity: Time O(H) | Space O(H) (where H is height)