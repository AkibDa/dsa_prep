# Problem: Group Anagrams

# Pattern: Hash Map (Grouping).

# Why: We need to group strings. The "key" for the group should be something common to all anagrams. Sorting the string (e.g., "eat" -> "aet") works as a perfect unique key.

import collections


def groupAnagrams(strs):
  ans = collections.defaultdict(list)

  for s in strs:
    # Create a key by sorting the string
    key = tuple(sorted(s))
    ans[key].append(s)

  return ans.values()

# Complexity: Time O(N ⚫ K log K) (where N is list length and K is max string length).