# Problem: Lowest Common Ancestor (LCA)

# Pattern: DFS (Post-order).

# Why: We search for p and q.
#     If root is p or q, return root.
#     If p and q are found in different subtrees (one left, one right), then root is the LCA.
#     If both are in the left subtree, the answer comes from the left.

def lowestCommonAncestor(root, p, q):
  if not root or root == p or root == q:
    return root

  left = lowestCommonAncestor(root.left, p, q)
  right = lowestCommonAncestor(root.right, p, q)

  if left and right:
    return root  # Found one on each side
  return left if left else right  # Either both on left or both on right

# Complexity: Time O(N) | Space O(H) (where H is height)