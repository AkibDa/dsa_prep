class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      raise IndexError("pop from empty stack")

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      raise IndexError("peek from empty stack")

  def size(self):
    return len(self.items)
  
  def display(self):
    return self.items
  
if __name__ == "__main__":
  s = Stack()
  s.push(10)
  s.push(20)
  s.push(30)
  print("Stack items:", s.display())
  print("Top item:", s.peek())
  print("Stack size:", s.size())
  print("Popped item:", s.pop())
  print("Stack items after pop:", s.display())