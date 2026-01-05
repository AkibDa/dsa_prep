# Problem: Find Median from Data Stream

# Pattern: Two Heaps (Min & Max).

# Why: To find the median, we need the middle element(s). We split the data into two halves:
#     Small Half: stored in a Max-Heap.
#     Large Half: stored in a Min-Heap.
#     Median is the top of the larger heap (or average of both tops).

import heapq

class MedianFinder:
  def __init__(self):
    # Python only has Min-Heap, so negate values for Max-Heap
    self.small = []  # Max-Heap
    self.large = []  # Min-Heap

  def addNum(self, num: int) -> None:
    heapq.heappush(self.small, -1 * num)

    # Ensure every num in small is <= every num in large
    if (self.small and self.large and
        (-1 * self.small[0]) > self.large[0]):
      val = -1 * heapq.heappop(self.small)
      heapq.heappush(self.large, val)

    # Balance sizes
    if len(self.small) > len(self.large) + 1:
      val = -1 * heapq.heappop(self.small)
      heapq.heappush(self.large, val)
    if len(self.large) > len(self.small) + 1:
      val = heapq.heappop(self.large)
      heapq.heappush(self.small, -1 * val)

  def findMedian(self) -> float:
    if len(self.small) > len(self.large):
      return -1 * self.small[0]
    if len(self.large) > len(self.small):
      return self.large[0]
    return (-1 * self.small[0] + self.large[0]) / 2

# Complexity: Time O(log N) (add), O(1) (find) | Space O(N)