def count_brave_soldiers(n):
  """
  Write your logic here.
  Parameters:
    n (int): The number of soldiers in the army
  Returns:
    int: The count of brave soldiers
  """
  """Checks if a number is prime."""
  if n < 2:
    return 0

  is_prime = [True] * (n + 1)
  is_prime[0] = is_prime[1] = False

  for p in range(2, int(n**0.5) + 1):
    if is_prime[p]:
      for i in range(p * p, n + 1, p):
        is_prime[i] = False

  return sum(is_prime)

def main():
  import sys
  input = sys.stdin.read
  n = int(input().strip())  # The input contains only one integer N
  
  # Call the user logic function and print the output
  result = count_brave_soldiers(n)
  print(result)

if __name__ == "__main__":
  main()