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
    
  def get_paths(self, start, end, path=None):
    if path is None:
      path = []
    path = path + [start]
    if start == end:
      return [path]
    if start not in self.graph_dict:
      return []
    paths = []
    for node in self.graph_dict[start]:
      if node not in path:
        sub_paths = self.get_paths(node, end)
        for path in sub_paths:
          paths.append([start] + path)
    return paths
  
  def get_shortest_path(self, start, end, path=None):
    if path is None:
      path = []
    path = path + [start]
    if start == end:
      return path
    if start not in self.graph_dict:
      return None
    shortest = None
    for node in self.graph_dict[start]:
      if node not in path:
        sp = self.get_shortest_path(node, end, path)
        if sp:
          if shortest is None or len(sp) < len(shortest):
            shortest = sp
    return  shortest
    
    
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
  shortest_path = route_graph.get_shortest_path("Mumbai", "New York")
  print("Shortest path from Mumbai to New York:")
  if shortest_path:
    print(" -> ".join(shortest_path))
  shortest_path = route_graph.get_shortest_path("Mumbai", "Toronto")
  print("Shortest path from Mumbai to Toronto:")
  if shortest_path:
    print(" -> ".join(shortest_path))
  shortest_path = route_graph.get_shortest_path("Paris", "Dubai")
  print("Shortest path from Paris to Dubai:")
  if shortest_path:
    print(" -> ".join(shortest_path))