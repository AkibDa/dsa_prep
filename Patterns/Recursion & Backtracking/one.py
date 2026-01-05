# Problem: Subsets

# Pattern: Backtracking (Pick vs. Don't Pick).

# Why: For every number, we have exactly two choices: include it in the current subset or exclude it. This creates a decision tree.

def subsets(nums):
  res = []
  subset = []

  def dfs(i):
    if i >= len(nums):
      res.append(subset.copy())
      return

    # Decision 1: Include nums[i]
    subset.append(nums[i])
    dfs(i + 1)

    # Decision 2: Exclude nums[i] (Backtrack)
    subset.pop()
    dfs(i + 1)

  dfs(0)
  return res

# Complexity: Time O(2^N) | Space O(N)