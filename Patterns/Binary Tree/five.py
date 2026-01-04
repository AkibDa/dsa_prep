# Problem: Balanced Binary Tree

# Pattern: DFS (Bottom-up).

# Why: Calculating height at every node from the top down is O(N^2). Instead, we return the height from the bottom. If a subtree is unbalanced, we return -1 (or a specific flag) to bubble the failure up immediately.

def isBalanced(root):
  def dfs(node):
    if not node: return 0

    left, right = dfs(node.left), dfs(node.right)

    # If any child is unbalanced or current node is unbalanced
    if left == -1 or right == -1 or abs(left - right) > 1:
      return -1

    return 1 + max(left, right)

  return dfs(root) != -1

# Complexity: Time O(N) | Space O(H) (where H is height)