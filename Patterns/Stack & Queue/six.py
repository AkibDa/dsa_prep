# Problem: Implement Queue using Stacks

# Pattern: Two Stacks.

# Why: A queue is FIFO, a stack is LIFO. Reversing a LIFO (popping everything from Stack 1 into Stack 2) gives you FIFO order.

class MyQueue:
  def __init__(self):
    self.s1 = []  # For pushing
    self.s2 = []  # For popping

  def push(self, x: int) -> None:
    self.s1.append(x)

  def pop(self) -> int:
    self.peek()
    return self.s2.pop()

  def peek(self) -> int:
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())
    return self.s2[-1]

  def empty(self) -> bool:
    return not self.s1 and not self.s2

# Complexity: Amortized O(1) per operation | Space O(N)