# Problem: House Robber

# Pattern: 1D DP (Decision Making).

# Why: At house i, you have two choices:
#     Rob it (add nums[i] + max loot from i-2).
#     Skip it (take max loot from i-1).

def rob(nums):
  rob1, rob2 = 0, 0

  for n in nums:
    # rob1 = loot from house i-2
    # rob2 = loot from house i-1
    newRob = max(n + rob1, rob2)
    rob1 = rob2
    rob2 = newRob

  return rob2

# Complexity: Time O(N) | Space O(1)