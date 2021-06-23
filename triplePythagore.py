def triplePythagore(limit):
  c, m = 0, 2

  while c < limit:
    for n in range(1, m):
      a = m * m - n * n
      b = 2 * m * n
      c = m * m + n * n

      if c > limit:
        break

      print(a, b, c)

    m = m + 1

if __name__ == '__main__' :
     
    limit = 100
    triplePythagore(limit)
 

