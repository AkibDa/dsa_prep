# Problem: Remove Nth Node From End of List

# Pattern: Two Pointers (Gap Method).

# Why: We don't know the length. If we move a right pointer N steps ahead first, and then move both left and right together, when right hits the end, left will be at the correct removal spot.

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def removeNthFromEnd(head, n):
  dummy = ListNode(0, head)
  left = dummy
  right = head

  # Move right n steps ahead
  while n > 0 and right:
    right = right.next
    n -= 1

  # Move both until right reaches end
  while right:
    left = left.next
    right = right.next

  # Delete node
  left.next = left.next.next
  return dummy.next

# Complexity: Time O(N) | Space O(1)