# Problem: Evaluate Reverse Polish Notation

# Pattern: Stack (Postfix Evaluation).

# Why: RPN is designed for stacks. Numbers go on the stack; operators pop the last two numbers, compute, and push the result back.

def evalRPN(tokens):
  stack = []
  for t in tokens:
    if t not in "+-*/":
      stack.append(int(t))
    else:
      b, a = stack.pop(), stack.pop()
      if t == "+":
        stack.append(a + b)
      elif t == "-":
        stack.append(a - b)
      elif t == "*":
        stack.append(a * b)
      elif t == "/":
        stack.append(int(a / b))  # Truncate toward zero
  return stack[0]

# Complexity: Time O(N) | Space O(N)