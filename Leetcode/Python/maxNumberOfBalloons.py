class Solution(object):
  def maxNumberOfBalloons(self, text):
    """
    :type text: str
    :rtype: int
    """
    if not text:
      return 0

    counts = {}

    for char in text:
      if char in counts:
        counts[char] += 1
      else:
        counts[char] = 1

    b = counts.get('b', 0)
    a = counts.get('a', 0)
    l = counts.get('l', 0) // 2
    o = counts.get('o', 0) // 2
    n = counts.get('n', 0)

    return min(b, a, l, o, n)