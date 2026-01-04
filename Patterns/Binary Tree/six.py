# Problem: Path Sum

# Pattern: DFS (Pre-order).

# Why: As we go down, we subtract the node's value from the targetSum. If we hit a leaf node and the remaining targetSum equals the leaf's value, we found a path.

def hasPathSum(root, targetSum):
  if not root:
    return False

  # Check if leaf and sum matches
  if not root.left and not root.right:
    return targetSum == root.val

  return (hasPathSum(root.left, targetSum - root.val) or
          hasPathSum(root.right, targetSum - root.val))

# Complexity: Time O(N) | Space O(H) (where H is height)