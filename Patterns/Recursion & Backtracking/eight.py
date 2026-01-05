# Problem: Palindrome Partitioning

# Pattern: Backtracking (String Slicing).

# Why: We check every possible prefix s[i:j+1]. If it's a palindrome, we snip it off and recurse on the rest of the string s[j+1:].

def partition(s):
  res = []
  part = []

  def dfs(i):
    if i >= len(s):
      res.append(part.copy())
      return

    for j in range(i, len(s)):
      if isPali(s, i, j):
        part.append(s[i: j + 1])
        dfs(j + 1)
        part.pop()

  def isPali(s, l, r):
    while l < r:
      if s[l] != s[r]: return False
      l, r = l + 1, r - 1
    return True

  dfs(0)
  return res

# Complexity: Time O(Nx2^N) | Space O(N)