#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:04:13 2020

@author: mar
archivo para probar genetic.py
"""
import genetic
import datetime
import unittest

def test_Hola_Mundo():
  objetivo = "coronavirus"
  adivine_contraseña(objetivo)
  
def adivine_contraseña(objetivo):
  geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!¡.,"
  horaInicio = datetime.datetime.now()
  def fnObtenerAptitud(genes):
    return obtener_aptitud(genes, objetivo)
  def fnMostrar(genes):
    mostrar(genes, objetivo, horaInicio)
    
  aptitudÓptima = len(objetivo)
  genetic.obtener_mejor(fnObtenerAptitud, len(objetivo), aptitudÓptima, geneSet, fnMostrar)
  

def obtener_aptitud(genes, objetivo):
  return sum(1 for esperado,real in zip (objetivo,genes)
             if esperado == real)
  
def mostrar(genes, objetivo, horaInicio):
  diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
  aptitud = obtener_aptitud(genes, objetivo)
  print("{}\t{}\t{}".format(genes,aptitud,diferencia))
  
if __name__ == '__main__':
  test_Hola_Mundo()

  