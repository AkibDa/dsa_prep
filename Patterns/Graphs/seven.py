# Problem: Graph Valid Tree

# Pattern: Union-Find (or DFS).

# Why: A valid tree must meet two conditions:
#     No cycles.
#     All nodes are connected (1 single component).
#     Union-Find detects cycles if we try to union two nodes that already share a parent.

def validTree(n, edges):
  if not n: return True
  adj = {i: [] for i in range(n)}
  for n1, n2 in edges:
    adj[n1].append(n2)
    adj[n2].append(n1)

  visit = set()

  def dfs(i, prev):
    if i in visit: return False  # Loop detected
    visit.add(i)
    for j in adj[i]:
      if j == prev: continue
      if not dfs(j, i): return False
    return True

  return dfs(0, -1) and n == len(visit)

# Complexity: Time O(V+E) | Space O(V)