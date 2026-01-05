# Problem: Recover Binary Search Tree

# Pattern: Inorder Traversal (Find Swapped Pair).

# Why: In a valid BST inorder traversal, values are always increasing (prev.val < cur.val). If this breaks, we found a swapped node.
#     First violation: prev is the first wrong node.
#     Second violation: curr is the second wrong node.

def recoverTree(root):
  # Variables to track the swapped nodes
  first = second = prev = None

  def inorder(node):
    nonlocal first, second, prev
    if not node: return

    inorder(node.left)

    # Check violation
    if prev and prev.val > node.val:
      if not first:
        first = prev
      second = node
    prev = node

    inorder(node.right)

  inorder(root)
  # Fix the swap
  first.val, second.val = second.val, first.val

# Complexity: Time O(N) | Space O(H) (where H is height)