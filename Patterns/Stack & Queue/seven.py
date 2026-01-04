# Problem: Simplify Path

# Pattern: Stack (String Parsing).

# Why: Directories work like a stack. '..' means pop (go back), '.' means do nothing, 'name' means push.

def simplifyPath(path):
  stack = []
  cur = ""

  for c in path + "/":
    if c == "/":
      if cur == "..":
        if stack: stack.pop()
      elif cur != "" and cur != ".":
        stack.append(cur)
      cur = ""
    else:
      cur += c

  return "/" + "/".join(stack)

# Complexity: Time O(N) | Space O(N)