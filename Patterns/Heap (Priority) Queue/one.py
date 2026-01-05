# Problem: Kth Largest Element in an Array

# Pattern: Min-Heap (of size K).

# Why: If we maintain a Min-Heap of size k, the heap will hold the k largest elements seen so far. The root of this heap (the smallest of the largest) is the k^th largest element.

import heapq

def findKthLargest(nums, k):
    # Method 1: Min-Heap of size k (O(N log K))
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# Complexity: Time O(N log K) | Space O(K)