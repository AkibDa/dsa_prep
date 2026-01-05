# Problem: Clone Graph

# Pattern: DFS + Hash Map.

# Why: We traverse the graph. To avoid infinite loops and re-creating nodes, we store a map of OriginalNode -> ClonedNode. If we see a node in the map, we return the clone immediately.

class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
  oldToNew = {}

  def dfs(node):
    if node in oldToNew:
      return oldToNew[node]

    copy = Node(node.val)
    oldToNew[node] = copy
    for nei in node.neighbors:
      copy.neighbors.append(dfs(nei))
    return copy

  return dfs(node) if node else None

# Complexity: Time O(V+E) | Space O(V)