class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
      return ""

    prefix = strs[0]

    for curr in strs[1:]:

      while not curr.startswith(prefix):
        prefix = prefix[:-1]

      if not prefix:
        return ""

    return prefix