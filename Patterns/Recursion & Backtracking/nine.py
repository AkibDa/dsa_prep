# Problem: Generate Parentheses

# Pattern: Backtracking (Rule-based).

# Why: We can add an opening bracket ( if open < n. We can add a closing bracket ) if closed < open.

def generateParenthesis(n):
  stack = []
  res = []

  def backtrack(openN, closedN):
    if openN == closedN == n:
      res.append("".join(stack))
      return

    if openN < n:
      stack.append("(")
      backtrack(openN + 1, closedN)
      stack.pop()

    if closedN < openN:
      stack.append(")")
      backtrack(openN, closedN + 1)
      stack.pop()

  backtrack(0, 0)
  return res

# Complexity: Time O(4^N/√N) (Catalan number) | Space O(N)