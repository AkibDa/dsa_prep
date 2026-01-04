# Problem: Palindrome Linked List

# Pattern: Fast & Slow Pointers + Reverse.

# Why: To check palindrome in O(1) space, we find the middle (slow/fast), reverse the second half of the list, and then compare the first half with the reversed second half.

def isPalindrome(head):
  fast, slow = head, head

  # Find middle (slow)
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

  # Reverse second half
  prev = None
  while slow:
    tmp = slow.next
    slow.next = prev
    prev = slow
    slow = tmp

  # Check palindrome
  left, right = head, prev
  while right:
    if left.val != right.val:
      return False
    left = left.next
    right = right.next
  return True

# Complexity: Time O(N) | Space O(1)