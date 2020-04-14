import random

def _generar_padre(longitud, geneSet):
  genes = []
  while len(genes) < longitud:
      tamañoMuestral = min(longitud-len(genes),len(geneSet))
      genes.extend(random.sample(geneSet,tamañoMuestral))
      return ''.join(genes)



def _mutar(padre, geneSet):
  índice = random.randrange(0, len(padre))
  genesDelNiño = list(padre)
  nuevoGen, alterno = random.sample(geneSet, 2)
  genesDelNiño[índice] = alterno if nuevoGen == genesDelNiño[
      índice] else nuevoGen
  return ''.join(genesDelNiño)


def obtener_mejor(obtener_aptitud, longitudObjetivo, aptitudÓptima, geneSet, mostrar):
  random.seed()
  mejorPadre = _generar_padre(longitudObjetivo, geneSet)
  mejorAptitud = obtener_aptitud(mejorPadre)
  mostrar(mejorPadre)
  if mejorAptitud >= aptitudÓptima:
    return mejorPadre
  while True:
    niño = _mutar(mejorPadre, geneSet)
    niñoAptitud = obtener_aptitud(niño)
    if mejorAptitud >= niñoAptitud:
      continue
    mostrar(niño)
    if niñoAptitud >= aptitudÓptima:
      return niño
    mejorAptitud = niñoAptitud
    mejorPadre = niño
    
    
    
    
    
