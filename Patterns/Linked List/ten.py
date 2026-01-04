# Problem: Flatten a Multilevel Doubly Linked List

# Pattern: DFS / Stack.

# Why: A child list is essentially a branch to explore immediately (Depth First). We can use a stack or simple recursion. Iterative stack is safer.

def flatten(head):
  if not head: return head
  curr = head

  while curr:
    if curr.child:
      # If next node exists, we must eventually come back to it
      # But here we do it in-place without explicit stack if we want
      # Or use pointer manipulation:

      next_node = curr.next
      child_node = curr.child

      curr.next = child_node
      child_node.prev = curr
      curr.child = None

      # Find the tail of the child list to connect back to next_node
      tail = child_node
      while tail.next:
        tail = tail.next

      tail.next = next_node
      if next_node:
        next_node.prev = tail

    curr = curr.next
  return head

# Complexity: Time O(N) | Space O(1) (Iterative pointer manipulation)