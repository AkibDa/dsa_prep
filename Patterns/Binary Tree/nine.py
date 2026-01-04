# Problem: Construct Binary Tree from Preorder and Inorder

# Pattern: Divide & Conquer

# Why:
#     Preorder tells us the root (first element).
#     Inorder allows us to see what is to the left of that root and what is to the right.

def buildTree(preorder, inorder):
  if not preorder or not inorder:
    return None

  root = TreeNode(preorder[0])
  mid = inorder.index(preorder[0])  # Find split point

  # Recursively build subtrees
  root.left = buildTree(preorder[1: mid + 1], inorder[:mid])
  root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
  return root

# Complexity: Time O(N^2) (due to .index() and slicing). Optimizable to O(N) using a Hash Map for inorder indices.