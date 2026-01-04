# Problem: Intersection of Two Linked Lists

# Pattern: Two Pointers (Synchronization).

# Why: The lists may have different lengths. If we traverse List A then List B, and simultaneously traverse List B then List A, both pointers will travel distance A+B. They will meet exactly at the intersection (or at None if no intersection).

def getIntersectionNode(headA, headB):
  l1, l2 = headA, headB

  while l1 != l2:
    l1 = l1.next if l1 else headB
    l2 = l2.next if l2 else headA

  return l1

# Complexity: Time O(N+M) | Space O(1)