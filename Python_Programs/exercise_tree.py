class TreeNode:
  def __init__(self, name, designation):
    self.name = name
    self.children = []
    self.parent = None
    self.designation = designation
    
  def add_child(self, child_node):
    child_node.parent = self
    self.children.append(child_node)
    
  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    return level
  
  def print_tree(self, property_name):
    if property_name == 'both':
      value = self.name + " (" + self.designation + ")"
    elif property_name == 'name':
      value = self.name
    else:
      value = self.designation

    spaces = ' ' * self.get_level() * 3
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + value)
    if self.children:
      for child in self.children:
        child.print_tree(property_name)
      
def build_company_tree():
  infra_head = TreeNode("Vishwa","Infrastructure Head")
  infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
  infra_head.add_child(TreeNode("Abhijit", "App Manager"))

  cto = TreeNode("Chinmay", "CTO")
  cto.add_child(infra_head)
  cto.add_child(TreeNode("Aamir", "Application Head"))

  hr_head = TreeNode("Gels","HR Head")

  hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
  hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

  ceo = TreeNode("Nilupul", "CEO")
  ceo.add_child(cto)
  ceo.add_child(hr_head)

  return ceo

if __name__ == "__main__":
  root_node = build_company_tree()
  root_node.print_tree("name")
  root_node.print_tree("designation")
  root_node.print_tree("both")