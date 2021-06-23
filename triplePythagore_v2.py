import numpy as np

def triplePythagore(nombreTriples):
  i = 0
  listeTriplePythagore = []
  a = [0, 0, 0]

  n = nombreTriples

  while i < n:
    if i%2 == 0:
      a[0] = i
      a[1] = int((i/2)**2 - 1)
      a[2] = int((i/2)**2 + 1)
    else:
      a[0] = i
      a[1] = int((i**2 - 1)/2)
      a[1] = int((i**2 + 1)/2)

    if a[0] < a[1] and a[0] < a[2] and np.gcd(a[0], a[1]) == np.gcd(a[0], a[2]) == np.gcd(a[1], a[2]):
        listeTriplePythagore.append((a[0], a[1], a[2]))
    else:
      n = n + 1

    i = i + 1

  return listeTriplePythagore

def codePythagoricien():
  return triplePythagore(26)


