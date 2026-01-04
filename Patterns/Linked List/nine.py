# Problem: Reorder List

# Pattern: Find Middle + Reverse + Merge.

# Why: The problem asks to interleave the first half with the reversed second half. This is a combination of 3 patterns: Fast/Slow to find middle, Reverse Linked List, and Merge Two Lists.

def reorderList(head):
  # Find middle
  slow, fast = head, head.next
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  # Reverse second half
  second = slow.next
  prev = slow.next = None
  while second:
    tmp = second.next
    second.next = prev
    prev = second
    second = tmp

  # Merge two halves
  first, second = head, prev
  while second:
    tmp1, tmp2 = first.next, second.next
    first.next = second
    second.next = tmp1
    first, second = tmp1, tmp2

# Complexity: Time O(N) | Space O(1)