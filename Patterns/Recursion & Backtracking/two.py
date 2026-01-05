# Problem: Permutations

# Pattern: Backtracking (Choices - Used).

# Why: At every step, we can pick any number that hasn't been picked yet.

def permute(nums):
  res = []

  def backtrack(curr):
    if len(curr) == len(nums):
      res.append(curr[:])
      return

    for n in nums:
      if n not in curr:  # Note: O(N) check; Set is faster
        curr.append(n)
        backtrack(curr)
        curr.pop()

  backtrack([])
  return res

# Complexity: Time O(NxN!) | Space O(N)