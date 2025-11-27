class Graph:
  def __init__(self, edges):
    self.edges = edges
    self.graph_dict = {}
    for start, end in edges:
      if start in self.graph_dict:
        self.graph_dict[start].append(end)
      else:
        self.graph_dict[start] = [end]
    print("Graph dictionary: ", self.graph_dict)
    
  def get_paths(self, start, end, path=[]):
    path = path + [start]
    paths = []
    if start == end:
      return [[start]]
    if start not in self.graph_dict:
      return []
    for node in self.graph_dict[start]:
      sub_paths = self.get_paths(node, end)
      for path in sub_paths:
        paths.append([start] + path)
    return paths
    
    
if __name__ == "__main__":
  routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
  ]
  
  route_graph = Graph(routes)
  print("All paths from Mumbai to New York:")
  all_paths = route_graph.get_paths("Mumbai", "New York")
  for path in all_paths:
    print(" -> ".join(path))
  print("All paths from Mumbai to Toronto:")
  all_paths = route_graph.get_paths("Mumbai", "Toronto")
  for path in all_paths:
    print(" -> ".join(path))
  print("All paths from Paris to Dubai:")
  all_paths = route_graph.get_paths("Paris", "Dubai")
  for path in all_paths:
    print(" -> ".join(path))