import collections

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        counts = collections.Counter(s)
        n = len(s)
        
        L = 0
        for i in range(n):
            if counts[target[i]] > 0:
                L += 1
                counts[target[i]] -= 1
            else:
                break
                
        start_i = min(L, n - 1)
        
        for j in range(L - 1, start_i - 1, -1):
            counts[target[j]] += 1
            
        for i in range(start_i, -1, -1):
            cand = None
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char > target[i] and counts[char] > 0:
                    cand = char
                    break
                    
            if cand is not None:
                counts[cand] -= 1
                rest = []
                
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if counts[char] > 0:
                        rest.append(char * counts[char])
                        
                return target[:i] + cand + "".join(rest)
                
            if i > 0:
                counts[target[i-1]] += 1
                
        return ""