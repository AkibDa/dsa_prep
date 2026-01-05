# Problem: Word Ladder

# Pattern: BFS (Shortest Path).

# Why: We want the shortest transformation sequence. In an unweighted graph, BFS guarantees the shortest path. Nodes are words; edges exist if words differ by 1 char.

import collections


def ladderLength(beginWord, endWord, wordList):
  if endWord not in wordList: return 0

  nei = collections.defaultdict(list)
  wordList.append(beginWord)
  for word in wordList:
    for j in range(len(word)):
      pattern = word[:j] + "*" + word[j + 1:]
      nei[pattern].append(word)

  visit = set([beginWord])
  q = collections.deque([beginWord])
  res = 1
  while q:
    for i in range(len(q)):
      word = q.popleft()
      if word == endWord: return res
      for j in range(len(word)):
        pattern = word[:j] + "*" + word[j + 1:]
        for neiWord in nei[pattern]:
          if neiWord not in visit:
            visit.add(neiWord)
            q.append(neiWord)
    res += 1
  return 0

# Complexity: Time O(M^2xN) (M=word len, N=list len) | Space O(M^2xN)