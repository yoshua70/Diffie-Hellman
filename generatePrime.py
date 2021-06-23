import random

def primesInRange(x, y):
  # Retourne tous les nombres premiers compris ente
  # x et y
  primeList = []
  for n in range(x, y):
    isPrime = True

    for num in range(2, n):
      if n % num == 0:
        isPrime = False

    if isPrime:
      primeList.append(n)

  return primeList

def generatePrime():
  return random.choice(primesInRange(7, 200))

print(generatePrime())