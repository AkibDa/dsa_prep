# Problem: Number of Connected Components

# Pattern: Union-Find (Disjoint Set Union).

# Why: We start with $N$ components. Every time we successfully union two distinct sets via an edge, we decrease the component count by 1.

def countComponents(n, edges):
  par = [i for i in range(n)]
  rank = [1] * n

  def find(n1):
    res = n1
    while res != par[res]:
      par[res] = par[par[res]]  # Path compression
      res = par[res]
    return res

  def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2: return 0

    if rank[p1] > rank[p2]:
      par[p2] = p1
      rank[p1] += rank[p2]
    else:
      par[p1] = p2
      rank[p2] += rank[p1]
    return 1

  res = n
  for n1, n2 in edges:
    res -= union(n1, n2)
  return res

# Complexity: Time O(E x ⍺(V)) (Inverse Ackermann function, nearly constant) | Space O(V)