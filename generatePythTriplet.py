import random

def singlePythTriplet(q):
  '''
  Génère un triplet pythagoricien à partir d'un entier non nul q.
  Retourne une liste de 3 coefficients correspondant aux coefficients du triplé pythagoricien. Les coefficients sont ordonnés.
  '''
  return [2*q + 1, q*(2*q + 2), q*(2*q + 2) + 1]

def pythTriplet(numberOfTriplets):
  '''
  Génère tous les triplets pythagoriciens possibles entre 1 et numberOfTriplets.
  Retourne une liste de triplés pythagoriciens.
  '''
  return [singlePythTriplet(q) for q in range(1, numberOfTriplets + 1)]
  # tripletList = []
  # for q in range(1, numberOfTriplets + 1):
  #   tripletList.append([2*q + 1, q*(2*q + 2), q*(2*q + 2) + 1])

  return tripletList

def generatePythTriplet():
  '''
  Génère un triplet pythagoricien aléatoire.
  '''
  q = random.randrange(1, 1000, 1)
  return [2*q + 1, q*(2*q + 2), q*(2*q + 2) + 1]
  