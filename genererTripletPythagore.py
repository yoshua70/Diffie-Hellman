import random
from genererPremier import genererNombrePremier

def tripletPythagoreModuloP(p):
  C = []
  compteur = 0
  
  for a in range(1, int((p-1)/2 + 1)):
    aa = a ** 2 % p
    for b in range(1, int((p-1)/2 + 1)):
      bb = b ** 2 % p
      for c in range(1, int((p-1)/2 + 1)):
        cc = c ** 2 % p
        if (aa + bb) % p == cc and a<=b:
          compteur = compteur + 1
          C.append([a, b, c])
          
  return C

def genererTripletPythagoreModuloP(p):
  return random.choice(tripletPythagoreModuloP(p))

def genererTPmodP():
  p = genererNombrePremier()
  return (random.choice(tripletPythagoreModuloP(p)), p)