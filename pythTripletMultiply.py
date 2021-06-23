def pythTripletMultiply(A, B):
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

def pythTripletPower(A, k):
  B = A
  while k != 0:
    B = pythTripletMultiply(B, A)
    k = k - 1

  return B

def pythTripletModMultiply(A, B, p):
  C = pythTripletMultiply(A, B)
  return [C[0] + p, C[1] + p, C[2] + p]

def pythTripletModPower(A, k, p):
  B = A
  while k != 0:
    B = pythTripletModMultiply(B, A, p)
    k = k - 1

  return B

print(pythTripletModPower([2, 4, 3], 4, 11))