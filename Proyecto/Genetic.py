import random as rand
import statistics
import time
import sys

# Seleccion de Progenitores
def _generar_padre(longitud, geneSet, obtener_aptitud):
    genes = []
    while len(genes) < longitud:
        tamañoMuestral = min(longitud - len(genes), len(geneSet))
        genes.extend(rand.sample(geneSet, tamañoMuestral))
    aptitud = obtener_aptitud(genes)
    return Cromosoma(genes, aptitud)


# Mutacion
def _mutar(padre, geneSet, obtener_aptitud):
    genesDelNiño = padre.Genes[:]
    indice = rand.randrange(0, len(padre.Genes))
    nuevoGen, alterno = rand.sample(geneSet, 2)
    genesDelNiño[indice] = alterno if nuevoGen == genesDelNiño[indice] else nuevoGen
    aptitud = obtener_aptitud(genesDelNiño)
    return Cromosoma(genesDelNiño, aptitud)

#Esta funcion nececita de la funcion que llama para la aptitud asi como  el numero de
#genes que se usaran para crear una nueva secuencia entre otros parametros
def obtener_mejor(obtener_aptitud, longitudObjetivo, aptitudOptima, geneSet, mostrar):
    rand.seed()
    def fnMutar(padre):
        return _mutar(padre, geneSet, obtener_aptitud)

    def fnGenerarPadre():
        return _generar_padre(longitudObjetivo, geneSet, obtener_aptitud)

    for mejora in _obtener_mejoras(fnMutar, fnGenerarPadre):
        mostrar(mejora)
        if not aptitudOptima > mejora.Aptitud:
            return mejora

# para mejorar la eficiencia de la funcion obtener_mejor 
# se divide el codigo del buble en 2 partes, primero generar secuencias mejore y
# despues enviarlas de vuelta atraves de yield.
def _obtener_mejoras(nuevo_niño, generar_padre):
    mejorPadre = generar_padre()
    yield mejorPadre
    while True:
        niño = nuevo_niño(mejorPadre)
        if mejorPadre.Aptitud > niño.Aptitud:
            continue
        if not niño.Aptitud > mejorPadre.Aptitud:
            mejorPadre = niño
            continue
        yield niño
        mejorPadre = niño
        
# Creacion de clase Cromosoma junto con su contructor y atributos
# Esto hara el motor gentico mas flexible.
class Cromosoma:
    def __init__(self, genes, aptitud):
        # definicion de atributos
        self.Genes = genes
        self.Aptitud = aptitud
# Evaluacion comparativa
# esta mejora contempla añadir soporte de evaluaciones comparativas
#ya que es muy util para conocer los tiempos de motor utilizando una clase.
class Comparar:
    def ejecutar(función):
        cronometrajes = []
        stdout = sys.stdout
        #esta funcion ejcuta la funcion proporcionada 100 veces e
        #informa el tiempo de cada ejecucion
        for i in range(100):
            sys.stdout = None
            horaInicio = time.time()
            función()
            segundos = time.time() - horaInicio
            sys.stdout = stdout
            cronometrajes.append(segundos)
            promedio = statistics.mean(cronometrajes)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(1 + i, promedio, statistics.stdev(cronometrajes, promedio) if i > 1 else 0))
                