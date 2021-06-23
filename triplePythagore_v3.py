import random

def triplePythagore(nombreTriples):
  
  listeTriples = []
  for q in range(1, nombreTriples + 1):
    listeTriples.append([2*q + 1, q*(2*q + 2), q*(2*q + 2) + 1])
  return listeTriples

def genererTriplePythagore():
  q = random.randrange(1, 1000, 1)
  return [2*q + 1, q*(2*q + 2), q*(2*q + 2) + 1]


def codePythagoricien():
  return triplePythagore(27)

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

#print(primesInRange(1, 200))

#print(genererTriplePythagore())

