#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplo de la clase 5 código gray como solución al problema binario no convergente
Created on Wed Mar  4 08:58:29 2020

@author: 
"""
import numpy as np
class CromosomaEntero():
  #def __init__(self):
  #  self.cromosoma = []
  representacion = "Gray"
  
  def __init__(self, numBits=8):
    #self.cromosoma = [0,0,0,0,0,0,0,0]
    """
    Convertir un cromosoma con valores psudoaleatorios de longitud numBIts
    """
    if(numBits>0):
      cromosoma = [0,0,0,0,0,1,1,0]
      self.cromosoma = np.array(cromosoma)
      
    
  def setRepresentacion(self, representacion):
    self.representacion = representacion
    
  def getFenotipo(self,):
    """
    Regresa el valor decimal correspondiente considerando la represenatcion (binaria o gray)
    """
    if self.representacion == "binario":
      #binario a decimal
      numBin=self.listaToString(self.cromosoma)
      #for i in range(0,self.cromosoma.size):
      #  numBin=numBin+str(self.cromosoma[i])
      #return int(numBin,2)
      return self.stringBinarioToDecimal(numBin)
    if self.representacion == "Gray":
      #gray decimal
      binUno = self.cromosoma
      binDos = self.cromosoma
      numBin=self.listaToString(binUno)
      binUno = np.append(binUno,0)
      #binUno = np.append(0,binUno)
      binDos = np.append(0,binDos)
      #binDos = np.append(binDos,0)
    
      numBin1= self.listaToString(binUno)
      numBin2= self.listaToString(binDos)
      #for i in range(0,binUno.size):
      #  numBin1=numBin1+str(binUno[i])
      #  numBin2=numBin2+str(binDos[i])
      sumaBin=""
      for i in range(0,len(numBin1)):
        if numBin1[i] == numBin2[i]:
          sumaBin = sumaBin+str("0")
        else:
          sumaBin = sumaBin+str("1")
          
      temp = len(sumaBin)
      gray = sumaBin[:temp-1] 
      Resultado = "Numero Gray: "+str(gray)+str("\nDecimal: ")+str(self.stringBinarioToDecimal(numBin))
      return Resultado
    
    
  def stringBinarioToDecimal(self, binario):
    return int(binario,2)
    
    
  def listaToString(self, lista):
    string = ""
    for element in lista:
      string=string+str(element)
    return string
    
#Inicio del programa
      
clf = CromosomaEntero()
clf.setRepresentacion("Gray")
var = clf.getFenotipo()
print(var)


    
    
    
    
    
    
    
    
    
    
    
    
    