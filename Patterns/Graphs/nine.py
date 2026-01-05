# Problem: Find Eventual Safe States

# Pattern: Topological Sort / Cycle Detection.

# Why: A "safe" node is one that does not lead to a cycle. We can use DFS with 3 states (0=unvisited, 1=visiting, 2=safe). If we finish visiting a node without detecting a cycle, it's safe.

def eventualSafeNodes(graph):
  n = len(graph)
  safe = {}

  def dfs(i):
    if i in safe: return safe[i]

    safe[i] = False  # Assume unsafe initially (cycle detection)
    for nei in graph[i]:
      if not dfs(nei):
        return False
    safe[i] = True  # Confirmed safe
    return True

  res = []
  for i in range(n):
    if dfs(i): res.append(i)
  return res

# Complexity: Time O(V+E) | Space O(V)