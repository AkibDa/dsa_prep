# Problem: Delete Node in a BST

# Pattern: Case Handling (0, 1, or 2 children).

# Why:
#     No children: Just delete.
#     One child: Replace node with its child.
#     Two children: Find the successor (smallest node in the right subtree), replace value, and recursively delete the successor.

def deleteNode(root, key):
  if not root: return None

  if key < root.val:
    root.left = deleteNode(root.left, key)
  elif key > root.val:
    root.right = deleteNode(root.right, key)
  else:
    # Case 1 & 2: 0 or 1 child
    if not root.left: return root.right
    if not root.right: return root.left

    # Case 3: 2 children - Find min in right subtree
    cur = root.right
    while cur.left:
      cur = cur.left
    root.val = cur.val
    root.right = deleteNode(root.right, cur.val)

  return root

# Complexity: Time O(H) | Space O(H) (where H is height)