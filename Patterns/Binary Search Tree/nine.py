# Problem: Trim a BST

# Pattern: Post-order restructuring.

# Why:
#     If the current node is too small (val < low), we discard it and return the result of trimming its right child (which might be valid).
#     If too big (val > high), return trimmed left child.
#     Otherwise, keep node and trim both children.

def trimBST(root, low, high):
  if not root: return None

  if root.val < low:
    return trimBST(root.right, low, high)
  if root.val > high:
    return trimBST(root.left, low, high)

  root.left = trimBST(root.left, low, high)
  root.right = trimBST(root.right, low, high)
  return root

# Complexity: Time O(N) | Space O(H) (where H is height)