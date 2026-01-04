# Problem: Min Stack

# Pattern: Two Stacks (or Stack of Tuples).

# Why: To get the minimum in O(1), we track the "minimum so far" alongside every value we push.

class MinStack:
  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    # Push to minStack only if it's smaller or equal to current min
    val = min(val, self.minStack[-1] if self.minStack else val)
    self.minStack.append(val)

  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minStack[-1]

# Complexity: Time O(1) | Space O(N)