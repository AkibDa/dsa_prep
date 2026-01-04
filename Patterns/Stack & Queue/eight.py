# Problem: Basic Calculator

# Pattern: Stack + Sign Tracking.

# Why: We iterate through the string. Parentheses '(' save the current state (result and sign) to the stack. ')' restores it.

def calculate(s):
  res = 0
  num = 0
  sign = 1
  stack = []

  for c in s:
    if c.isdigit():
      num = num * 10 + int(c)
    elif c in ["+", "-"]:
      res += sign * num
      num = 0
      sign = 1 if c == "+" else -1
    elif c == "(":
      stack.append(res)
      stack.append(sign)
      sign = 1
      res = 0
    elif c == ")":
      res += sign * num
      num = 0
      res *= stack.pop()  # pop sign
      res += stack.pop()  # pop prev result

  return res + sign * num

# Complexity: Time O(N) | Space O(N)