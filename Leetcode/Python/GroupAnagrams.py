import collections

def groupAnagrams(strs):
    ans = collections.defaultdict(list)

    for s in strs:
        # 1. Create a frequency array of size 26 (for a-z)
        count = [0] * 26
        
        # 2. Count each character
        for c in s:
            # ord(c) gives ASCII value. ord(c) - ord('a') maps 'a'->0, 'b'->1...
            count[ord(c) - ord('a')] += 1
        
        # 3. Use the count array (converted to tuple) as the key
        ans[tuple(count)].append(s)

    return ans.values()