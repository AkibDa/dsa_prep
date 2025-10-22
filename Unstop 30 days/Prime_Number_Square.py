n = int(input())

def isPrime(num):

  if num <= 1:
    return False

  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False

  return True

if n <= 0:
    print("Please enter a positive integer.")
else:
    prime_count = 0
    current_number = 1
    nth_prime = 0
    
    while prime_count < n:
      current_number += 1
      if isPrime(current_number):
        prime_count += 1
    
    nth_prime = current_number
    
    print(f"{nth_prime * nth_prime}")