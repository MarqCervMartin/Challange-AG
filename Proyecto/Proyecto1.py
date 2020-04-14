#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:20:38 2020

@author: mar

Implementar un AG en Python para ordenación de una lista de números.
Basarse en el archivo anexo.
Se evalúa de manera similar a los laboratorios anteriores.
"""
import random
import unittest
import datetime
#import genetic

def obtener_aptitud(genes):
  #devuelve el número de genes que están en orden ascendente
  aptitud = 1
  for i in range(1,len(genes)):
    if genes[i] > genes[i-1]:
      aptitud+=1
    return aptitud
  
def mostrar(candidato, horaInicio):
  #muestra los genes actuales, su aptitud y el tiempo transcurrido
  #ejemplo: 53, 74, 95 => 3 0:00:00,001004
  diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
  print("{}\t=> {}\t{}".format(', '.join(map(str, candidato.Genes)),candidato.Aptitud,diferencia))
 
  
class PruebasDeNumerosOrdenados(unittest.TestCase):
  def test_ordenar_3_números(self):
    self.ordenar_números(3)
    
  def ordenar_números(self, númerosTotales):
    geneSet = [i for i in range(100)]
    #inicia un temporizador
    #crea las funciones auxiliares y la aptitud óptima
    #después llama a 'genetic'.obtener_mejor()
    #finalmente, asevera que la aptitud del resultado es óptima
    

random.seed()
#Genera la hora de inicio
horaInicio = datetime.datetime.now()
#Genera el primer padre, como parametro el valor de la pass
clf = PruebasDeNumerosOrdenados()
clf.test_ordenar_3_números()
#Calcula la aptitud del primer padre
#mejorAptitud = obtener_aptitud(mejorPadre)
#Muestra el primer padre desde la aptitud, hasta la diferencia medida en segundos
#mostrar(mejorPadre)
    
    
    
    
    
    
  

