# Problem: Invert Binary Tree

# Pattern: DFS (Pre-order).

# Why: At every node, we simply swap its left and right children. Then we tell the children to do the same.

def invertTree(root):
  if not root:
    return None

  # Swap children
  root.left, root.right = root.right, root.left

  # Recurse
  invertTree(root.left)
  invertTree(root.right)
  return root

# Complexity: Time O(N) | Space O(H) (where H is height)