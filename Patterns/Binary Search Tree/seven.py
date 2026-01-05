# Problem: Convert Sorted Array to BST

# Pattern: Divide & Conquer (Middle Element).

# Why: To make a balanced BST, the middle element of the array must be the root. The left half of the array becomes the left child, and the right half becomes the right child.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def sortedArrayToBST(nums):
  def helper(l, r):
    if l > r:
      return None

    mid = (l + r) // 2
    root = TreeNode(nums[mid])
    root.left = helper(l, mid - 1)
    root.right = helper(mid + 1, r)
    return root

  return helper(0, len(nums) - 1)

# Complexity: Time O(N) | Space O(logN)