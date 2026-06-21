class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0

    insertIndex = 1

    for i in range(1, len(nums)):

      if nums[i] != nums[i - 1]:
        nums[insertIndex] = nums[i]
        insertIndex += 1

    return insertIndex