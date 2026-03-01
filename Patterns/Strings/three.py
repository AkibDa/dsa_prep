# Problem: Group Anagrams

# Pattern: Hash Map (Grouping).

# Why: We need to group strings. The "key" for the group should be something common to all anagrams. Sorting the string (e.g., "eat" -> "aet") works as a perfect unique key.

def groupAnagram(strs):
  ans = {}
  
  for s in strs:
    key = "".sorted(s)
    
    if key not in ans:
      ans[key] = []
        
    ans[key].append(s)
      
  return list(ans.values())

# Complexity: Time O(N ⚫ K log K) (where N is list length and K is max string length).