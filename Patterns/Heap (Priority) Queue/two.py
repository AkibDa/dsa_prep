# Problem: Top K Frequent Elements

# Pattern: HashMap + Min-Heap.

# Why: First count frequencies (O(N)). Then, use a heap to keep the top k frequencies.

import collections, heapq


def topKFrequent(nums, k):
  count = collections.Counter(nums)
  heap = []

  for num, freq in count.items():
    heapq.heappush(heap, (freq, num))
    if len(heap) > k:
      heapq.heappop(heap)

  return [num for freq, num in heap]

# Complexity: Time O(N log K) | Space O(N)