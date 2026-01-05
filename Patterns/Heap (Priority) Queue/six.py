# Problem: Reorganize String

# Pattern: Max-Heap (Greedy).

# Why: To avoid adjacent duplicates, always pick the character with the highest remaining frequency that is different from the previous one.

import collections, heapq

def reorganizeString(s):
  count = collections.Counter(s)
  maxHeap = [[-cnt, char] for char, cnt in count.items()]
  heapq.heapify(maxHeap)

  prev = None
  res = ""

  while maxHeap or prev:
    if not maxHeap and prev: return ""  # Impossible

    cnt, char = heapq.heappop(maxHeap)
    res += char
    cnt += 1  # Decrement count (it was negative)

    if prev:
      heapq.heappush(maxHeap, prev)
      prev = None

    if cnt != 0:
      prev = [cnt, char]

  return res

# Complexity: Time O(N log 26) which is O(N) | Space O(1)