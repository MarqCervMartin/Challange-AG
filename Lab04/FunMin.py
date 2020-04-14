#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:10:10 2020

@author: mar
"""

#gray random
#gray a decimal
#calcular aptitud

#
import random
import datetime

geneSet = "10101"
objetivo = "00000"



def generar_padre(longitud):
    genes = []
    while len(genes) < longitud:
        tamañoMuestral = min(longitud - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, tamañoMuestral))
    return ''.join(genes)
  
  
  
def obtener_aptitud(conjetura):
    conjetura = int(conjetura,2)
    apti = pow(conjetura-15,2)
    return apti
    #return sum(1 for esperado, real in zip(objetivo, conjetura)
    #           if esperado == real)


def mostrar(conjetura):
    diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
    aptitud = obtener_aptitud(conjetura)
    print("{}\t{}\t{}".format(conjetura, aptitud, diferencia))


def mutar(padre):
    índice = random.randrange(0, len(padre))
    genesDelNiño = list(padre)
    nuevoGen, alterno = random.sample(geneSet, 2)
    genesDelNiño[índice] = alterno if nuevoGen == genesDelNiño[
        índice] else nuevoGen
    return ''.join(genesDelNiño)



random.seed()
horaInicio = datetime.datetime.now()
mejorPadre = generar_padre(len(objetivo))
mejorAptitud = obtener_aptitud(mejorPadre)
mostrar(mejorPadre)

while True:
    niño = mutar(mejorPadre)
    niñoAptitud = obtener_aptitud(niño)
    if mejorAptitud <= niñoAptitud:
        continue
    mostrar(niño)
    if niñoAptitud <= len(mejorPadre):
        break
    mejorAptitud = niñoAptitud
    mejorPadre = niño








