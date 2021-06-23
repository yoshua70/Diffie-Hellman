import random

def primesInRange(x, y):
  prime_list = []
  for n in range(x, y):
      isPrime = True

      for num in range(2, n):
          if n % num == 0:
              isPrime = False

      if isPrime:
          prime_list.append(n)
          
  return prime_list

def genererNombrePremier():
  return random.choice(primesInRange(7, 100))