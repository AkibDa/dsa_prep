# Problem: Combination Sum

# Pattern: Backtracking (Unbounded Knapsack).

# Why: We can choose the same number multiple times.
#     Left branch: Choose current number again (stay at i).
#     Right branch: Don't choose current number (move to i + 1).

def combinationSum(candidates, target):
  res = []

  def dfs(i, cur, total):
    if total == target:
      res.append(cur.copy())
      return
    if i >= len(candidates) or total > target:
      return

    # Include candidates[i]
    cur.append(candidates[i])
    dfs(i, cur, total + candidates[i])

    # Skip candidates[i]
    cur.pop()
    dfs(i + 1, cur, total)

  dfs(0, [], 0)
  return res

# Complexity: Time O(2^T) (loosely, where T is target) | Space O(T)