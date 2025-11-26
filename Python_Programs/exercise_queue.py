import threading
import time
from collections import deque

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
  
  def front(self):
    return self.buffer[-1]

  
food_order_queue = Queue()

def place_orders(orders):
  for order in orders:
    print(f"Placing order for {order}...")
    food_order_queue.enqueue(order)
    print(f"Order for {order} placed.")
    time.sleep(0.5)
    
def serve_orders():
  time.sleep(1)
  while not food_order_queue.is_empty():
    order = food_order_queue.dequeue()
    print("Serving order for ", order)
    time.sleep(2)
  print("All orders have been served.")  
  
def produce_binary_numbers(n):
  q = Queue()
  q.enqueue("1")
  
  result = []
  
  for _ in range(n):
    front = q.front()
    print("  ", front)
    q.enqueue(front + "0")
    q.enqueue(front + "1")
  
    q.dequeue()
    
if __name__ == "__main__":
  orders = ['pizza','samosa','pasta','biryani','burger']
  t1 = threading.Thread(target=place_orders, args=(orders,))
  t2 = threading.Thread(target=serve_orders)

  # t1.start()
  # t2.start()
  
  produce_binary_numbers(10)