class Solution:
  def minimumDeletions(self, nums: List[int]) -> int:
    i_min = nums.index(min(nums))
    i_max = nums.index(max(nums))
    
    a = min(i_min, i_max)
    b = max(i_min, i_max)
    n = len(nums)
    
    both_front = b + 1
    both_back = n - a
    front_and_back = (a + 1) + (n - b)
    
    return min(both_front, both_back, front_and_back)