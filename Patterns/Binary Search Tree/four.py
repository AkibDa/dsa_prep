# Problem: Lowest Common Ancestor of a BST

# Pattern: BST Split Logic.

# Why: Unlike a normal tree, we know where to look.
#      If both p and q are smaller than root, go Left.
#      If both are greater, go Right.
#      If one is smaller and one is larger (or one is the root), this is the split point (LCA).

def lowestCommonAncestor(root, p, q):
  cur = root

  while cur:
    if p.val < cur.val and q.val < cur.val:
      cur = cur.left
    elif p.val > cur.val and q.val > cur.val:
      cur = cur.right
    else:
      return cur

# Complexity: Time O(H) | Space O(1) (where H is height)