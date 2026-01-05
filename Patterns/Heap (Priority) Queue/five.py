# Problem: Task Scheduler

# Pattern: Max-Heap + Queue.

# Why: Always process the most frequent task available (Max-Heap). If a task is processed, it goes into a "cooldown queue" and can't be added back to the heap until time passes.

import collections, heapq

def leastInterval(tasks, n):
  count = collections.Counter(tasks)
  maxHeap = [-cnt for cnt in count.values()]
  heapq.heapify(maxHeap)

  time = 0
  q = collections.deque()  # pairs of [-cnt, idleTime]

  while maxHeap or q:
    time += 1
    if maxHeap:
      cnt = 1 + heapq.heappop(maxHeap)
      if cnt:
        q.append([cnt, time + n])

    if q and q[0][1] == time:
      heapq.heappush(maxHeap, q.popleft()[0])

  return time

# Complexity: Time O(N) | Space O(1) (max 26 letters)