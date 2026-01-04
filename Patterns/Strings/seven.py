# Problem: Valid Parentheses

# Pattern: Stack.

# Why: The last opened bracket must be the first one closed (LIFO).

def isValid(s):
  stack = []
  closeToOpen = {")": "(", "]": "[", "}": "{"}

  for c in s:
    if c in closeToOpen:
      if stack and stack[-1] == closeToOpen[c]:
        stack.pop()
      else:
        return False
    else:
      stack.append(c)

  return True if not stack else False

# Complexity: Time O(N) | Space O(N)