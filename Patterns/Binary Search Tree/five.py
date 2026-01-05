# Problem: Kth Smallest Element in a BST

# Pattern: Inorder Traversal.

# Why: Inorder traversal of a BST always yields sorted values. We just iterate until we hit the k^th node.

def kthSmallest(root, k):
  stack = []
  curr = root

  while stack or curr:
    while curr:
      stack.append(curr)
      curr = curr.left

    curr = stack.pop()
    k -= 1
    if k == 0:
      return curr.val

    curr = curr.right

# Complexity: Time O(H+k) | Space O(H) (where H is height)