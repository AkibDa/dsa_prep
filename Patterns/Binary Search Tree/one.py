# Problem: Validate Binary Search Tree

# Pattern: DFS with Range Constraints.

# Why: A node must not only be greater than its left child, but greater than everything in its left subtree. We pass down a valid range (min_val, max_val) for each node.

def isValidBST(root):
  def valid(node, left, right):
    if not node:
      return True
    if not (left < node.val < right):
      return False

    return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))

  return valid(root, float("-inf"), float("inf"))

# Complexity: Time O(N) | Space O(H) (where H is height)