# Problem: Valid Parentheses

# Pattern: Stack (LIFO).

# Why: We need to match the most recent opening bracket with the current closing bracket.

def isValid(s):
  stack = []
  mapping = {")": "(", "}": "{", "]": "["}

  for char in s:
    if char in mapping:
      # Check if stack is not empty and matches
      if stack and stack[-1] == mapping[char]:
        stack.pop()
      else:
        return False
    else:
      stack.append(char)

  return not stack

# Complexity: Time O(N) | Space O(N)