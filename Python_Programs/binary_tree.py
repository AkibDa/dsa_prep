class BinarySearchTreeNode:
  
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    
  def insert(self, data):
    if data < self.data:
      if self.left is None:
        self.left = BinarySearchTreeNode(data)
      else:
        self.left.insert(data)
    else:
      if self.right is None:
        self.right = BinarySearchTreeNode(data)
      else:
        self.right.insert(data)
        
  def search(self, data):
    if self.data == data:
      return True
    elif data < self.data:
      if self.left:
        return self.left.search(data)
      else:
        return False
    else:
      if self.right:
        return self.right.search(data)
      else:
        return False
      
  def inorder_traversal(self):
    elements = []
    if self.left:
      elements += self.left.inorder_traversal()
      
    elements.append(self.data)
    
    if self.right:
      elements += self.right.inorder_traversal()
      
    return elements
  
  def preorder_traversal(self):
    elements = []
    elements.append(self.data)
    
    if self.left:
      elements += self.left.preorder_traversal()
      
    if self.right:
      elements += self.right.preorder_traversal()
      
    return elements
  
  def postorder_traversal(self):
    elements = []
    
    if self.left:
      elements += self.left.postorder_traversal()
      
    if self.right:
      elements += self.right.postorder_traversal()
      
    elements.append(self.data)
    
    return elements
  
  def find_min(self):
    if self.left is None:
      return self.data
    return self.left.find_min()
  
  def delete_node(self, data):
    if data < self.data:
      if self.left:
        self.left = self.left.delete_node(data)
    elif data > self.data:
      if self.right:
        self.right = self.right.delete_node(data)
    else:
      if self.left is None and self.right is None:
        return None
      elif self.left is None:
        return self.right
      elif self.right is None:
        return self.left
      else:
        min_larger_node = self.right
        while min_larger_node.left:
          min_larger_node = min_larger_node.left
        self.data = min_larger_node.data
        self.right = self.right.delete_node(min_larger_node.data)
    return self
  
def build_tree(elements):
  root = BinarySearchTreeNode(elements[0])
  
  for i in range(1, len(elements)):
    root.insert(elements[i])
    
  return root

if __name__ == "__main__":
  numbers = [17,4,1,20,9,23,18,34]
  bst = build_tree(numbers)
  
  print("Inorder Traversal:", bst.inorder_traversal())
  print("Preorder Traversal:", bst.preorder_traversal())
  print("Postorder Traversal:", bst.postorder_traversal())
  
  print("Minimum value in the BST:", bst.find_min())
  
  search_values = [20, 5]
  for value in search_values:
    found = bst.search(value)
    print(f"Value {value} found in BST:" , found)