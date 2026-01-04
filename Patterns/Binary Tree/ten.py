# Problem: Symmetric Tree

# Pattern: DFS (Dual Tree).

# Why: A tree is symmetric if the Left Subtree is a mirror reflection of the Right Subtree. We compare two nodes t1 and t2 simultaneously. t1.left must match t2.right.

def isSymmetric(root):
  def dfs(t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False

    return (t1.val == t2.val and
            dfs(t1.left, t2.right) and
            dfs(t1.right, t2.left))

  return dfs(root.left, root.right) if root else True

# Complexity: Time O(N) | Space O(H) (where H is height)