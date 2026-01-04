# Problem: Reverse Linked List

# Pattern: In-Place Reversal.

# Why: We need to change the direction of pointers without using extra memory. We maintain three pointers: prev, curr, and next.

def reverseList(head):
  prev, curr = None, head

  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  return prev

# Complexity: Time O(N) | Space O(1)