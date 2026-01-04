# Problem: Copy List with Random Pointer

# Pattern: Hash Map (Old -> New).

# Why: We cannot copy pointers directly because the nodes they point to might not exist yet.
#     First pass: Create new nodes and map Old_Node -> New_Node.
#     Second pass: Assign next and random pointers using the map.

class Node:
  def __init__(self, val=0, next=None, random=None):
    self.val = val
    self.next = next
    self.random = random

def copyRandomList(head):
  oldToCopy = {}

  cur = head
  while cur:
    copy = Node(cur.val)
    oldToCopy[cur] = copy
    cur = cur.next

  cur = head
  while cur:
    copy = oldToCopy[cur]
    copy.next = oldToCopy.get(cur.next)
    copy.random = oldToCopy.get(cur.random)
    cur = cur.next

  return oldToCopy.get(head)

# Complexity: Time O(N) | Space O(N)