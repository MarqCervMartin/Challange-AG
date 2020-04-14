#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:59:03 2020

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
import unittest
import datetime
import genetic
import operator
import functools
import random

class PruebaDeCartas(unittest.TestCase):
  #Se ejecutara en primer lugar la función test
  def test(self):
    #losta por comprensión de 10 elementos
    geneSet = [i+1 for i in range(10)]
    #Obtenemos hora exacta
    horaInicio = datetime.datetime.now()
    #Mostramos Cadidato
    def fnMostrar(candidato):
      mostrar(candidato, horaInicio)
    #Obtenemos aptitud
    def fnObtenerAptitud(genes):
      return obtener_aptitud(genes)
    
    def fnMutar(genes):
      mutar(genes, geneSet)
      
    aptitudÓptima = Aptitud(36, 360, 0)
    
    #De genetic obtenemos el mejor gen
    mejor = genetic.obtener_mejor(fnObtenerAptitud, 10, aptitudÓptima, geneSet, fnMostrar, mutación_personalizada=fnMutar)
    self.assertTrue(not aptitudÓptima > mejor.Aptitud)

def obtener_aptitud(genes):
  #Obtenemos la suma de los primeros 5 genes
  sumaDelGrupo1 = sum(genes[0:5])
  #multiplicamos el resto
  productoDelGrupo2 = functools.reduce(operator.mul, genes[5:10])
  #obtenemos los genes duplicados
  duplicados = (len(genes)-len(set(genes)))
  #retornamos la aptitud con tres parametros
  return Aptitud(sumaDelGrupo1, productoDelGrupo2, duplicados)

class Aptitud:
  #constructor
  def __init__(self, sumaDelGrupo1, productoDelGrupo2, duplicados):
    #Definimos las variables y haremos referencia con self
    self.SumaDelGrupo1 = sumaDelGrupo1
    self.ProductoDelGrupo2 = productoDelGrupo2
    #las diferencias se refieren a un valor absoluto en este caso nos interesa el producto
    # de 360 y la suma de 36
    diferenciaSuma = abs(36-sumaDelGrupo1)
    diferenciaProducto = abs(360-productoDelGrupo2)
    self.DiferenciaTotal = diferenciaSuma + diferenciaProducto
    self.Duplicados = duplicados
    
  #método gt compara dos aptitudes y nos quedaremos con la secuencia con menos duplicados
  def __gt__(self, otro):
    if self.Duplicados != otro.Duplicados:
      return self.Duplicados < otro.Duplicados
    return self.DiferenciaTotal < otro.DiferenciaTotal
  
  
  #método string que nos regresa strin en formato de las variables suma grupo 1 ,2 y los duplicados
  def __str__(self):
    return "sum: {} prod: {} dups: {}".format(self.SumaDelGrupo1, self.ProductoDelGrupo2, self.Duplicados)
  
#para el método mostrar pasamos como parametro el gen candidato y la hora donde se creo para medir tiempo
def mostrar(candidato, horaInicio):
  #calculamos la diferencia en segundos
  diferencia = (datetime.datetime.now()-horaInicio).total_seconds()
  print("{} - {}\t{}\t{}".format(', '.join(map(str, candidato.Genes[0:5])),', '.join(map(str, candidato.Genes[5:10])),candidato.Aptitud,diferencia))


if __name__ == '__main__':
    unittest.main()
    
#la función mutar recibe como parametros el gen y el set del gen
def mutar(genes, geneSet):
  #si genes es igual en longitud con el set de genes:
    if len(genes) == len(set(genes)):
      #contador de 1 a 4
        cuenta = random.randint(1, 4)
        #si contador es mayor a 0
        while cuenta > 0:
          #se resta uno
            cuenta -= 1
            #obtiene los indices
            índiceA, índiceB = random.sample(range(len(genes)), 2)
            #mutan los indices
            genes[índiceA], genes[índiceB] = genes[índiceB], genes[índiceA]
            
    else:
      #intercambio de dos genes
        índiceA = random.randrange(0, len(genes))
        índiceB = random.randrange(0, len(geneSet))
        genes[índiceA] = geneSet[índiceB]

"""
def test(self):
  geneSet = [i+1 for i in range(10)]
  horaInicio = datetime.datetime.now()
  def fnMostrar(candidato):
    mostrar(candidato, horaInicio)
  def fnObtenerAptitud(genes):
    return obtener_aptitud(genes)
  
  aptitudÓptima = Aptitud(36, 360, 0)
  mejor = genetic.obtener_mejor(fnObtenerAptitud, 10, aptitudÓptima, geneSet, fnMostrar)
  self.assertTrue(not aptitudÓptima > mejor.Aptitud)


  xd = [i for i in numeros if i>5]
  len(xd)
  xd1 = [0 if i<=5 else 1 for i in numeros]
  
  
  lst3=[1 if e%2==0 else 0 for e in lst] 
  
  x=1
  for i in range(5):
    x+=1
  print(x)
  
  gallina produce eggs en dias
  3/2 -> 3/2 = 3/2
  9 ->36 =x
  6 ->9->1
  
  days = 
  
  gallina + eggs + days = 0
  days = 

"""
  
  
