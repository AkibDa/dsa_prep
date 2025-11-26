queue = []

queue.insert(0, 'a')  # enqueue
queue.insert(0, 'b')  # enqueue
queue.insert(0, 'c')  # enqueue
print("Initial queue:", queue)
print("Dequeue:", queue.pop())  # dequeue
print("Queue after dequeue:", queue)

from collections import deque
queue = deque()
queue.appendleft('a')  # enqueue
queue.appendleft('b')  # enqueue
queue.appendleft('c')  # enqueue
print("Initial queue using deque:", queue)
print("Dequeue from deque:", queue.pop())  # dequeue
print("Deque after dequeue:", queue)

class Queue:
  def __init__(self):
    self.buffer = deque()
    
  def is_empty(self):
    return len(self.buffer) == 0
  
  def enqueue(self, item):
    self.buffer.appendleft(item)
    
  def dequeue(self):
    if not self.is_empty():
      return self.buffer.pop()
    else:
      raise IndexError("dequeue from empty queue")
    
  def size(self):
    return len(self.buffer)
  
  def display(self):
    return list(self.buffer)
  
if __name__ == "__main__":
  pq = Queue()
  pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
  })
  pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
  })
  pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
  })
  print("Queue items:", pq.display())
  print("Queue size:", pq.size())
  print("Dequeue item:", pq.dequeue())
  print("Queue items after dequeue:", pq.display())