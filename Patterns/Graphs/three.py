# Problem: Course Schedule

# Pattern: Topological Sort / Cycle Detection.

# Why: A course prerequisite structure is a Directed Graph. If there is a cycle (A requires B, B requires A), it's impossible. We use DFS with 3 states: visiting, visited, unvisited.

def canFinish(numCourses, prerequisites):
  preMap = {i: [] for i in range(numCourses)}
  for crs, pre in prerequisites:
    preMap[crs].append(pre)

  visit = set()  # currently visiting

  def dfs(crs):
    if crs in visit: return False  # Cycle detected
    if preMap[crs] == []: return True

    visit.add(crs)
    for pre in preMap[crs]:
      if not dfs(pre): return False
    visit.remove(crs)
    preMap[crs] = []  # Mark as completed
    return True

  for crs in range(numCourses):
    if not dfs(crs): return False
  return True

# Complexity: Time O(V+E) | Space O(V+E)