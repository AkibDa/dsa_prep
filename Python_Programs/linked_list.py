class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node
    
  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
    
    itr = self.head
    llstr = ''
    while itr:
      llstr += str(itr.data) + ' --> '
      itr = itr.next
    print(llstr)
    
  def delete_at_beginning(self):
    if self.head is None:
      print("Linked list is empty, nothing to delete")
      return
    self.head = self.head.next
    
  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
    
    itr = self.head
    while itr.next:
      itr = itr.next
      
    itr.next = Node(data, None)
    
  def delete_at_end(self):
    if self.head is None:
      print("Linked list is empty, nothing to delete")
      return
    
    if self.head.next is None:
      self.head = None
      return
    
    itr = self.head
    while itr.next.next:
      itr = itr.next
      
    itr.next = None
    
  def get_length(self):
    if self.head is None:
      return 0
    
    count = 0
    itr = self.head
    while itr:
      count += 1
      itr = itr.next
    return count
  
  def clear(self):
    self.head = None
    
if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_at_beginning(5)
  ll.insert_at_beginning(10)
  ll.insert_at_beginning(15)
  ll.print()
  ll.delete_at_beginning()
  ll.print()
  ll.insert_at_end(20)
  ll.print()
  ll.delete_at_end()
  ll.print()
  print("Length of linked list:", ll.get_length())