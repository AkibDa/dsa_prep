# Problem: Network Delay Time

# Pattern: Dijkstra’s Algorithm.

# Why: We have a weighted directed graph and need the shortest time to reach all nodes. Dijkstra is standard for weighted shortest paths with non-negative weights.

import heapq
import collections


def networkDelayTime(times, n, k):
  edges = collections.defaultdict(list)
  for u, v, w in times:
    edges[u].append((v, w))

  minHeap = [(0, k)]  # (time, node)
  visit = set()
  t = 0

  while minHeap:
    w1, n1 = heapq.heappop(minHeap)
    if n1 in visit: continue
    visit.add(n1)
    t = max(t, w1)

    for n2, w2 in edges[n1]:
      if n2 not in visit:
        heapq.heappush(minHeap, (w1 + w2, n2))

  return t if len(visit) == n else -1

# Complexity: Time O(ElogV) | Space O(V+E)