import random

def primesInRange(x, y):
  '''
  Retourne tous les nombres premiers compris entre x et y.
  x et y sont des entiers.
  '''
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
  '''
  Génère un nombre premier aléatoire compris entre 7 et 200.
  '''
  return random.choice(primesInRange(7, 200))

print(generatePrime())