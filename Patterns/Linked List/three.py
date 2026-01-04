# Problem: Linked List Cycle

# Pattern: Fast & Slow Pointers (Floyd’s Cycle-Finding).

# Why: If there is a cycle, a fast pointer (moving 2 steps) will eventually lap/catch up to a slow pointer (moving 1 step). If they meet, a cycle exists.

def hasCycle(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

# Complexity: Time O(N) | Space O(1)