#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:44:29 2020

@author: mar
"""
import random
import numpy as np
palabra = input("Ingrese una palabra: ").lower()

print(palabra)
n = 10 #Número de individuos en la población
#poblacion = []
cantidadLetras = len(palabra)

def crearPoblacion(cantidad):
  poblacion = []
  for i in range(n):
    palabra = ""
    
    for letra in range(cantidad):
      numero = random.randint(97,122) #generamos codigo ascii
      palabra = palabra + chr(numero) #insertamos el codigo en chr y lo interpreta
    
    poblacion.append(palabra) #agregamos palabra a la poblacion, a la lista
    #end for 2
  #end for 1
  return poblacion


def evaluacion(poblacion, palabra):
  puntuaciones = []
  for individuo in poblacion: 
    puntaje = 0
    for indice in range(len(individuo)):
      if individuo[indice] == palabra[indice]:
        puntaje+=1
    puntuaciones.append(puntaje)
  return puntuaciones
  

def seleccionNatural(poblacion, puntuaciones):
  indices = np.argsort(puntuaciones)[::-1]
  #print(poblacion, puntuaciones)
  #print(indices)
  seleccionados = []
  
  #  [hola, queso, llamas]
  #  0       1       2 
  #  1       2       3
  
  for indice in indices[:3]:
    seleccionados.append(poblacion[indice])
  #seleccionados.append(poblacion[len(indices) - 1])

  while True:
    
    i = 1
    if poblacion[indice] not in seleccionados:
      seleccionados.append(poblacion[-i])
      break
    i+=1
  
  while True:
    indice = random.choice(indices)
    
    if poblacion[indice] not in seleccionados:
      seleccionados.append(poblacion[indice])
      return seleccionados
      

def cruzamiento(seleccionados):
  poblacion = []
    
  for individuo in range (n):
    padres = random.choice(seleccionados, k=3)  
    palabra = ""
    for letra in range(cantidadDeLetras):
      numeros = random.randint(0,100)
      
      if numero > 70:
        palabra += palabra + padres[0][letra]
      elif numero < 30:
        palabra = palabra + padres[1][letra]
      else:
        palabra = palabra + padres[2][letra]
    poblacion.append(palabra)
  return poblacion


def mutacion(poblacion):
  mutados = []
  for individuo in poblacion:
    numero = random.randint(0,100)
    #mutado =
    if numero<=50:
      for letra in individuo:
        numero = random.randint(0,100)
        if numero >= 70:
          mutado = mutado +chr(random.randint)
    else:
      mutado = individuo
      
    mutados.append(mutado)

poblacion = crearPoblacion(cantidadLetras)

HighScore = 0
generacion = 0


while HighScore < len(palabra):
  puntuaciones = evaluacion(poblacion,palabra)
  
  print("generacion: ",generacion)
  HighScore = max(puntuaciones)
  print("HighScore: ",HighScore)
  print("Mejor JUgador: ",poblacion[puntuaciones.index(HighScore)])
  generacion+=1
  seleccionados = seleccionNatural(poblacion, puntuaciones)
  poblacion = cruzamiento(seleccionados)
  poblacion = mutacion(poblacion)

#puntuaciones = evaluacion(poblacion,palabra)
#seleccionados = seleccionNatural(poblacion, puntuaciones)
#cruzamiento(sleccionados)



















