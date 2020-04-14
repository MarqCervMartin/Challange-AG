#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:57:48 2020

@author: mar

Universidad Autónoma del Estado de México
Centro Universitario UAEM Zumpango
Ingeniería en Computación
UA Algoritmos Genéticos 2020-A
Alumno(s): Márquez Cervantes Martín
Paterno Materno Nombre(s)
Profesor: Dr. Asdrúbal López Chau
Descripción:Proyecto 02.
Problema de las cartas

Fecha: 8 de Abril 2020
"""

import random as rand
import statistics
import time
import sys

#La función recibe por parametros la longitud, el set y el valor de aptitud para no tener colisiones
def _generar_padre(longitud, geneSet, obtener_aptitud):
    genes = []
    while len(genes) < longitud:
        tamañoMuestral = min(longitud - len(genes), len(geneSet))
        genes.extend(rand.sample(geneSet, tamañoMuestral))
    aptitud = obtener_aptitud(genes)
    return Cromosoma(genes, aptitud)


# LA funcion mutar es el motor del AG el cual cambia un indice con rand sample obtiene un valor del genSet
def _mutar(padre, geneSet, obtener_aptitud):
    genesDelNiño = padre.Genes[:]
    indice = rand.randrange(0, len(padre.Genes))
    nuevoGen, alterno = rand.sample(geneSet, 2)
    genesDelNiño[indice] = alterno if nuevoGen == genesDelNiño[indice] else nuevoGen
    aptitud = obtener_aptitud(genesDelNiño)
    return Cromosoma(genesDelNiño, aptitud)

#Con está función anidada obtenemos la mejor aptitud
def obtener_mejor(obtener_aptitud, longitudObjetivo, aptitudÓptima, geneSet, mostrar, mutación_personalizada=None):
    rand.seed()
    if mutación_personalizada is None:
      def fnMutar(padre):
        return _mutar(padre, geneSet, obtener_aptitud)
    else:
      def fnMutar(padre):
        return _mutar_personalizada(padre, mutación_personalizada, obtener_aptitud)
        
    #def fnMutar(padre):
    #    return _mutar(padre, geneSet, obtener_aptitud)

    def fnGenerarPadre():
        return _generar_padre(longitudObjetivo, geneSet, obtener_aptitud)

    for mejora in _obtener_mejoras(fnMutar, fnGenerarPadre):
        mostrar(mejora)
        if not aptitudÓptima > mejora.Aptitud:
            return mejora

#nuestra función mutación personalizada nos permitira hacer dos cambios a la vez
def _mutar_personalizada(padre, mutación_personalizada, obtener_aptitud):
  
    genesDelNiño = padre.Genes[:]
    mutación_personalizada(genesDelNiño)
    aptitud = obtener_aptitud(genesDelNiño)
    return Cromosoma(genesDelNiño, aptitud)

#con esta funcioón Obtenemos una eficiencia del AG
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
        
#La clase cromosoma hara más flexible el modulo genetic, cremos genes y aptitud
class Cromosoma:
    def __init__(self, genes, aptitud):
        self.Genes = genes
        self.Aptitud = aptitud

class Comparar:
    def ejecutar(función):
        cronometrajes = []
        stdout = sys.stdout
        #obtenemos un benchmar con statistics el cual evalua la función 100 veces y obtiene una media
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

