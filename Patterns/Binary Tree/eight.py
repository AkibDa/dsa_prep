# Problem: Serialize and Deserialize Binary Tree

# Pattern: DFS (Pre-order).

# Why: To reconstruct a tree uniquely, we need to record null pointers (e.g., as "N"). Pre-order traversal is easiest to process for reconstruction because the first element is always the root.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Codec:
  def serialize(self, root):
    res = []

    def dfs(node):
      if not node:
        res.append("N")
        return
      res.append(str(node.val))
      dfs(node.left)
      dfs(node.right)

    dfs(root)
    return ",".join(res)

  def deserialize(self, data):
    vals = data.split(",")
    self.i = 0

    def dfs():
      if vals[self.i] == "N":
        self.i += 1
        return None
      node = TreeNode(int(vals[self.i]))
      self.i += 1
      node.left = dfs()
      node.right = dfs()
      return node

    return dfs()

# Complexity: Time O(N) | Space O(N)