def triplePythagoreSurP(nombreTriples, p):
  n = 0
  q = 1
  listeTriples = []
  while n < nombreTriples:
    u = 2*q + 1
    v = q*(2*q + 2)
    w = q*(2*q + 2) + 1

    if((u**2 + v**2) % p == w**2):
      listeTriples.append([u, v, w])
      print(u, v, w)
      n = n + 1
    else:
      nombreTriples = nombreTriples + 1
    q = q + 1
  return listeTriples

def loiTriplePythagoreSurP(A, B, p):
  a = A[0]
  b = A[1]
  c = A[2]
  
  x = B[0]
  y = B[1]
  z = B[2]

  u = a*x + b*y + p
  v = abs(a*y - b*x) + p
  w = c*z + p

  return [u, v, w]

def loiTriplePythagorePuissance(A, k):
  B = A
  while k != 0:
    B = loiTriplePythagoreSurP(B, A)
    k = k - 1

  return B

def invLoiPythagore(A, p):
  a = A[0]
  b = A[1]
  c = A[2]

  u = (a/(c**2)) + p
  v = ((b/a)*u) + p
  w = (1/c) + p

  return [u, v, w]

#A = [5, 12, 13]

#B = invLoiPythagore(A, 7)
#print(B)
#print(loiTriplePythagoreSurP(A, B, 7))

