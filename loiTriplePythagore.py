def loiTriplePythagore(A, B):
  a = A[0]
  b = A[1]
  c = A[2]
  
  x = B[0]
  y = B[1]
  z = B[2]

  u = a*x + b*y
  v = abs(a*y - b*x)
  w = c*z

  return [u, v, w]

def loiTriplePythagorePuissance(A, k):
  B = A
  while k != 0:
    B = loiTriplePythagore(B, A)
    k = k - 1

  return B
