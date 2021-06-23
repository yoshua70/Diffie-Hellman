import random

def pythTriplet(numberOfTriplets):
  tripletList = []
  for q in range(1, numberOfTriplets + 1):
    tripletList.append([2*q + 1, q*(2*q + 2), q*(2*q + 2) + 1])

  return tripletList

def generatePythTriplet():
  q = random.randrange(1, 1000, 1)
  return [2*q + 1, q*(2*q + 2), q*(2*q + 2) + 1]
  