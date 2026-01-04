# Problem: Sliding Window Maximum

# Pattern: Monotonic Queue (Deque).

# Why: We need to keep the maximum in the window. We use a deque to store indices.
#     Remove indices that are out of the current window from the front.
#     Remove indices whose values are smaller than the current value from the back (they can never be the max again).
#     The front of the deque is always the index of the max value.

import collections


def maxSlidingWindow(nums, k):
  output = []
  q = collections.deque()  # stores indices
  l = 0

  for r in range(len(nums)):
    # Remove smaller values from back
    while q and nums[q[-1]] < nums[r]:
      q.pop()
    q.append(r)

    # Remove values out of window from front
    if l > q[0]:
      q.popleft()

    if (r + 1) >= k:
      output.append(nums[q[0]])
      l += 1

  return output

# Complexity: Time O(N) | Space O(K)