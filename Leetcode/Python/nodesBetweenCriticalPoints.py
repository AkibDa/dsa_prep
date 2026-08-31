# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_critical = -1
        last_critical = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        index = 1
        
        while curr.next:
            nxt = curr.next
            
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                
                if first_critical == -1:
                    first_critical = index
                else:
                    min_dist = min(min_dist, index - last_critical)
                
                last_critical = index
            
            prev = curr
            curr = nxt
            index += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
            
        max_dist = last_critical - first_critical
        
        return [min_dist, max_dist]