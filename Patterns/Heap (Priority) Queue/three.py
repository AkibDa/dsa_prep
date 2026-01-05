# Problem: Merge K Sorted Lists

# Pattern: Min-Heap (Dijkstra-like).

# Why: We always want the smallest current node among all k lists. Push the head of every list into a Min-Heap. Pop the smallest, add to result, and push that node's .next back into the heap.

import heapq

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def mergeKLists(lists):
  minHeap = []

  # Add first node of each list
  for i, l in enumerate(lists):
    if l: heapq.heappush(minHeap, (l.val, i, l))

  dummy = ListNode()
  curr = dummy

  while minHeap:
    val, i, node = heapq.heappop(minHeap)
    curr.next = node
    curr = curr.next

    if node.next:
      heapq.heappush(minHeap, (node.next.val, i, node.next))

  return dummy.next

# Complexity: Time O(N log K) | Space O(K)