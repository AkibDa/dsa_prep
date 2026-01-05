# Problem: Sliding Window Median

# Pattern: Two Heaps (Lazy Removal).

# Why: Same logic as "Find Median from Data Stream", but elements leave the window. Since removing from a heap is O(N), we "lazily" mark them as invalid in a Hash Map and only remove them when they float to the top of the heap.

import heapq

def medianSlidingWindow(nums, k):
  small, large = [], []  # Max-Heap, Min-Heap
  balance = 0

  def remove(heap, element):
    # Note: True lazy removal is complex to implement concisely.
    # This is a conceptual O(N) removal for clarity in interviews.
    # In real production, use "Lazy Removal" with a dict.
    ind = heap.index(element)
    heap[ind] = heap[-1]
    heap.pop()
    heapq.heapify(heap)

  res = []
  for i, n in enumerate(nums):
    # Add new
    if not small or n <= -small[0]:
      heapq.heappush(small, -n)
    else:
      heapq.heappush(large, n)

    # Remove old (out of window)
    if i >= k:
      out = nums[i - k]
      if out <= -small[0]:
        remove(small, -out)
      else:
        remove(large, out)

    # Rebalance
    while len(small) > len(large) + 1:
      heapq.heappush(large, -heapq.heappop(small))
    while len(large) > len(small):
      heapq.heappush(small, -heapq.heappop(large))

    if i >= k - 1:
      if k % 2 == 1:
        res.append(-small[0])
      else:
        res.append((-small[0] + large[0]) / 2)
  return res

# Complexity: Time O(NxK) due to simplified removal. O(N log K) with full lazy deletion implementation.