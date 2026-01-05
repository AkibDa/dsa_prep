# Problem: K Closest Points to Origin

# Pattern: Max-Heap (size K).

# Why: We want the K smallest distances. By maintaining a Max-Heap of size K, we keep track of the "closest" points found so far. If a new point is closer than the farthest point in our heap (the root), we swap them.

import heapq

def kClosest(points, k):
  maxHeap = []

  for x, y in points:
    dist = -(x ** 2 + y ** 2)  # Negate for Max-Heap
    heapq.heappush(maxHeap, [dist, x, y])

    if len(maxHeap) > k:
      heapq.heappop(maxHeap)

  return [[x, y] for dist, x, y in maxHeap]

# Complexity: Time O(N log K) | Space O(K)