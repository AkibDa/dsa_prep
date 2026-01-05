# Problem: Range Sum of BST

# Pattern: DFS with Pruning.

# Why: We don't need to visit every node.
#      If node.val < low, the whole left subtree is useless (too small), so only go Right.
#      If node.val > high, the whole right subtree is useless (too big), so only go Left.

def rangeSumBST(root, low, high):
  if not root: return 0

  if root.val < low:
    return rangeSumBST(root.right, low, high)
  elif root.val > high:
    return rangeSumBST(root.left, low, high)

  return (root.val +
          rangeSumBST(root.left, low, high) +
          rangeSumBST(root.right, low, high))

# Complexity: Time O(N) (worst case) | Space O(H) (where H is height)