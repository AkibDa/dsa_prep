class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None
    
  def add_child(self, child):
    child.parent = self
    self.children.append(child)
    
def build_product_tree():
  root = TreeNode("Electronics")
  
  laptop = TreeNode("Laptop")
  laptop.add_child(TreeNode("MacBook"))
  laptop.add_child(TreeNode("Surface"))
  laptop.add_child(TreeNode("ThinkPad"))
  
  cellphone = TreeNode("Cell Phone")
  cellphone.add_child(TreeNode("iPhone"))
  cellphone.add_child(TreeNode("Google Pixel"))
  cellphone.add_child(TreeNode("Vivo"))
  
  tv = TreeNode("TV")
  tv.add_child(TreeNode("Samsung"))
  tv.add_child(TreeNode("LG"))
  
  root.add_child(laptop)
  root.add_child(cellphone)
  root.add_child(tv)
  
  return root
    
if __name__ == "__main__":
  product_tree = build_product_tree()
  print("Root Node:", product_tree.data)
  for child in product_tree.children:
    print(" Child Node:", child.data)
    for grandchild in child.children:
      print("  Grandchild Node:", grandchild.data)