# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:57:23 2015

@author: Nicolas Gentil e Nicolas Fonteyne

Projeto 3

"""

from formulas_utilizadas import *

alimentos = open('alimentos.csv', encoding="latin1")          #Abrindo a lista de alimentos
usuario = open('usuario.csv',encoding="latin1")          #Abrindo a lista do usuário

a = alimentos.readlines()          #Lendo a lista de alimentos
u = usuario.readlines()          #Lendo a lista do usuário

#Organizando a lista do usuário

info = u[1].strip().split(",")          #Fazendo com que as palavras de uma linha fiquem em linhas separadas

for p in info:        
    print(p)
        
print('')


for l in u[3:]:          #Criando uma timeline de alimentos ingeridos pelo usuário
    b = l.strip().split(",")    
    for pedaço in b:
        print(pedaço)
     
#Criando o dicionário

dic_al = {}     

#Organizando a lista de alimentos

for e in a[1:]:
    pedacos = e.strip().split(",")
    dic_al[pedacos[0]] = [float(pedacos[1]), float(pedacos[2]), float(pedacos[3]), float(pedacos[4]), float(pedacos[5])]
    #pedaço 1 = gramas / 2 = kcalorias / 3 = proteínas / 4 = carboidratos / 5 = gorduras

#print(dic_al) 

info [1] = float(info[1])
info [2] = float(info[2])         #fazendo com que os elementos numéricos da lista info passem para o formato float
info[4] = float(info[4])

# calorias que deveria consumir:

print('')


if info[3] == 'M':
    
    result = formula_de_hb_m(info[2], info[4], info[1], info[5])
   
if info[3] == 'F':
    
    result = formula_de_hb_f(info[2], info[4], info[1], info[5])
    
print('KCALORIAS QUE DEVERIA CONSUMIR POR DIA:', result)
 

    


         


