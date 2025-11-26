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
  
    
if __name__ == "__main__":
  orders = ['pizza','samosa','pasta','biryani','burger']
  t1 = threading.Thread(target=place_orders, args=(orders,))
  t2 = threading.Thread(target=serve_orders)

  t1.start()
  t2.start()