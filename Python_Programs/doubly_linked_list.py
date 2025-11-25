class Node:
  def __init__(self, data=None, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev
    
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_beginning(self, data):
    node = Node(data, self.head, None)
    if self.head:
      self.head.prev = node
    self.head = node
    
  def print_forward(self):
    if self.head is None:
      print("Doubly linked list is empty")
      return
    
    itr = self.head
    llstr = ''
    while itr:
      llstr += str(itr.data) + ' => '
      itr = itr.next
    print(llstr)
    
  def print_backward(self):
    if self.head is None:
      print("Doubly linked list is empty")
      return
    
    itr = self.head
    while itr.next:
      itr = itr.next
      
    llstr = ''
    while itr:
      llstr += str(itr.data) + ' <= '
      itr = itr.prev
    print(llstr)
    
  def delete_at_beginning(self):
    if self.head is None:
      print("Doubly linked list is empty, nothing to delete")
      return
    self.head = self.head.next
    if self.head:
      self.head.prev = None
    
  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None, None)
      return
    
    itr = self.head
    while itr.next:
      itr = itr.next
      
    new_node = Node(data, None, itr)
    itr.next = new_node
    
  def delete_at_end(self):
    if self.head is None:
      print("Doubly linked list is empty, nothing to delete")
      return
    
    if self.head.next is None:
      self.head = None
      return
    
    itr = self.head
    while itr.next:
      itr = itr.next
      
    itr.prev.next = None

if __name__ == "__main__":
  dll = DoublyLinkedList()
  dll.insert_at_end(10)
  dll.insert_at_end(20)
  dll.insert_at_beginning(5)
  dll.print_forward()  # Output: 5 => 10 => 20 => 
  dll.print_backward()  # Output: 20 => 10 => 5 <=
  dll.delete_at_beginning()
  dll.print_forward()  # Output: 10 <= 20 <= 
  dll.print_backward()  # Output: 20 <= 10 <=
  dll.delete_at_end()
  dll.print_forward()  # Output: 10 =>
  dll.print_backward()  # Output: 10 <=