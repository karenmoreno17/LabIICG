

def redondear(a):
  return int(a + 0.5)

def dda(x1, y1, x2, y2) -> list:
  listaX = []
  listaY = []
  lista = []
  x, y = x1, y1
  largo = abs((x2-x1) if abs(x2-x1) > abs(y2-y1) else (y2-y1))
  dx = (x2 - x1)/float(largo)
  dy = (y2 - y1)/float(largo)
  listaX.append(redondear(x))
  listaY.append(redondear(y))
  for i in range(largo):
    x += dx
    y += dy
    listaX.append(redondear(x))
    listaY.append(redondear(y))
  lista.append(listaX)
  lista.append(listaY)
  return lista