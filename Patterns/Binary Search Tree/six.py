# Problem: BST Iterator

# Pattern: Controlled Inorder Traversal (Stack).

# Why: We pause the inorder traversal. The stack holds the "ancestry" needed to find the next smallest node.

class BSTIterator:
  def __init__(self, root):
    self.stack = []
    self._push_left(root)

  def _push_left(self, node):
    while node:
      self.stack.append(node)
      node = node.left

  def next(self) -> int:
    node = self.stack.pop()
    if node.right:
      self._push_left(node.right)
    return node.val

  def hasNext(self) -> bool:
    return len(self.stack) > 0

# Complexity: Time O(1) amortized | Space O(H) (where H is height)