from generatePythTriplet import singlePythTriplet 


def generatePythCode(message):
  '''
  Génère un message codé sur la base des triplés pythagoriciens.
  Chaque lettre du message est codé en un triplet à l'aide de son code ASCII.
  La fonction retourne une liste de triplets pythagoriciens.
  '''
  return [singlePythTriplet(ord(char)) for char in message]

def decodePythCode(triplet):
  '''
  Décode un message initialement codé sur la base des triplés pythagoriciens.
  Réalise l'opération inverse de la fonction generatePythCode().
  La fonction retourne un string correspondant au message initialement codé.
  '''
  message = ""
  for t in triplet:
   for q in range(32, 127):
    
      if singlePythTriplet(q) == t:
        message = message + chr(q)

  return message
