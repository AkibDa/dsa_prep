# Problem: Maximum Depth of Binary Tree

# Pattern: DFS (Post-order).

# Why: The depth of a node is 1 (itself) plus the maximum depth of its children. We compute from the bottom up.

def maxDepth(root):
  if not root:
    return 0
  return 1 + max(maxDepth(root.left), maxDepth(root.right))

# Complexity: Time O(N) | Space O(H) (where H is height)