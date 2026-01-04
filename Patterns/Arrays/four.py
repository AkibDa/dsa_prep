# Problem: Merge Intervals

# Pattern: Sorting + Merging.

# Why: Overlapping intervals can only be identified efficiently if they are ordered. Sort by start time, then check if the current interval overlaps with the previous one.

def merge(intervals):
  intervals.sort(key=lambda x: x[0])
  output = [intervals[0]]

  for start, end in intervals[1:]:
    lastEnd = output[-1][1]

    if start <= lastEnd:
      output[-1][1] = max(lastEnd, end)
    else:
      output.append([start, end])
  return output

# Complexity: Time O(N logN) | Space O(N)