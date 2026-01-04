# Problem: Diameter of Binary Tree

# Pattern: DFS (Post-order with Global State).

# Why: The longest path might not pass through the root. At any specific node, the longest path through that node is height(left) + height(right). We calculate height normally, but update a global max_diameter variable at every step.

def diameterOfBinaryTree(root):
  res = 0

  def height(node):
    nonlocal res
    if not node: return 0

    left = height(node.left)
    right = height(node.right)

    # Diameter through this node
    res = max(res, left + right)

    # Return height to parent
    return 1 + max(left, right)

  height(root)
  return res

# Complexity: Time O(N) | Space O(H) (where H is height)