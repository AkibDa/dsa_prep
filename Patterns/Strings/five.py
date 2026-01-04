# Problem: String to Integer (atoi)

# Pattern: State Simulation (Parsing).

# Why: No complex algorithm, just careful handling of states: 1. Whitespace, 2. Sign, 3. Digits, 4. Overflow.

def myAtoi(s):
  s = s.strip()
  if not s:
    return 0

  sign = 1
  index = 0
  if s[index] == '+':
    index += 1
  elif s[index] == '-':
    index += 1
    sign = -1

  res = 0
  while index < len(s) and s[index].isdigit():
    digit = int(s[index])
    # Check overflow (conceptually, though Python handles large ints)
    if res > (2 ** 31 - 1 - digit) // 10:
      return 2 ** 31 - 1 if sign == 1 else -2 ** 31

    res = res * 10 + digit
    index += 1

  res = sign * res
  # Clamp to 32-bit integer range
  if res > 2 ** 31 - 1: return 2 ** 31 - 1
  if res < -2 ** 31: return -2 ** 31
  return res

# Complexity: Time O(N) | Space O(1)