# Problem: Combination Sum II

# Pattern: Backtracking (Handling Duplicates).

# Why: Similar to Subsets, but we sort the input first. If we choose to skip a number, we must skip all identical numbers following it to avoid duplicate combinations.

def combinationSum2(candidates, target):
  candidates.sort()
  res = []

  def backtrack(i, cur, total):
    if total == target:
      res.append(cur[:])
      return
    if total > target or i == len(candidates):
      return

    # Include candidates[i]
    cur.append(candidates[i])
    backtrack(i + 1, cur, total + candidates[i])
    cur.pop()

    # Skip duplicates
    while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
      i += 1
    backtrack(i + 1, cur, total)

  backtrack(0, [], 0)
  return res

# Complexity: Time O(2^N) | Space O(N)