# Problem: Add Two Numbers

# Pattern: Elementary Math (Carry Handling).

# Why: We simulate school-book addition. Iterate through the lists, sum the digits plus any carry, and create a new node for the digit.

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def addTwoNumbers(l1, l2):
  dummy = ListNode()
  cur = dummy
  carry = 0

  while l1 or l2 or carry:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0

    # New digit
    val = v1 + v2 + carry
    carry = val // 10
    val = val % 10
    cur.next = ListNode(val)

    # Update ptrs
    cur = cur.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None

  return dummy.next

# Complexity: Time O(N) | Space O(N) (for result list)