# Problem: Smallest Range Covering Elements from K Lists

# Pattern: Min-Heap (Tracking Max).

# Why: Like "Merge K Lists", but we track the current range max_val - min_val. The Min-Heap gives us the min_val. We explicitly track max_val as we push.

import heapq

def smallestRange(nums):
  minHeap = []
  currentMax = float('-inf')

  for i in range(len(nums)):
    heapq.heappush(minHeap, (nums[i][0], i, 0))  # val, list_idx, el_idx
    currentMax = max(currentMax, nums[i][0])

  resRange = [float('-inf'), float('inf')]

  while minHeap:
    minVal, listIdx, i = heapq.heappop(minHeap)

    if currentMax - minVal < resRange[1] - resRange[0]:
      resRange = [minVal, currentMax]

    if i + 1 < len(nums[listIdx]):
      nextVal = nums[listIdx][i + 1]
      heapq.heappush(minHeap, (nextVal, listIdx, i + 1))
      currentMax = max(currentMax, nextVal)
    else:
      break

  return resRange

# Complexity: Time O(N log K) | Space O(K)