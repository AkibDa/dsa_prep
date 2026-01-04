# Problem: Merge Two Sorted Lists

# Pattern: Two Pointers (with Dummy Node).

# Why: Since both lists are sorted, we can look at the head of both and pick the smaller one to append to our result. A "dummy" node simplifies edge cases (handling the head of the new list).

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def mergeTwoLists(list1, list2):
  dummy = ListNode()
  tail = dummy

  while list1 and list2:
    if list1.val < list2.val:
      tail.next = list1
      list1 = list1.next
    else:
      tail.next = list2
      list2 = list2.next
    tail = tail.next

  if list1:
    tail.next = list1
  elif list2:
    tail.next = list2

  return dummy.next

# Complexity: Time O(N+M) | Space O(1)