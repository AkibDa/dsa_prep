# Problem: Binary Tree Inorder Traversal

# Pattern: DFS (Recursive).

# Why: Inorder means visiting nodes in the order: Left -> Root -> Right.

def inorderTraversal(root):
  res = []

  def dfs(node):
    if not node: return
    dfs(node.left)  # 1. Left
    res.append(node.val)  # 2. Root
    dfs(node.right)  # 3. Right

  dfs(root)
  return res

# Complexity: Time O(N) | Space O(N) (recursion stack)