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

#Criando os dicionários

dic_al = {}  
dic_gramas = {}
dic_dias = {}

#Organizando a lista do usuário

info = u[1].strip().split(",")          #Fazendo com que as palavras de uma linha fiquem em linhas separadas na vírgula

for p in info:        
    print(p)
        
print('')

lista = []

#Criando uma timeline de alimentos ingeridos pelo usuário

for l in u[3:]:

    b = l.strip().split(",") 
    lista.append(b)
    
    for pedaço in b:
        print(pedaço)

print(' ')

#Organizando a lista de alimentos

#Adicionando os elementos no dic_al:

for e in a[1:]:
    pedacos = e.strip().split(",")
    dic_al[pedacos[0]] = [float(pedacos[1]), float(pedacos[2]), float(pedacos[3]), float(pedacos[4]), float(pedacos[5])]
    #pedaço 1 = gramas / 2 = kcalorias / 3 = proteínas / 4 = carboidratos / 5 = gorduras

#adicionando os elementos ao dic_gramas:

for e in lista:
    dic_gramas[e[1]] = e[2]
print(dic_gramas)

#Adicionando os elementos ao dic_dias:
listavalues = []
for e in lista:
    dic_dias[e[0]] = listavalues
    listavalues.append(e[1])
        
print('')  
print(dic_dias)

#Fazendo com que os elementos numéricos da lista info passem para o formato float

info [1] = float(info[1])
info [2] = float(info[2])         
info [4] = float(info[4])

# calorias que deveria consumir:

print('')

if info[3] == 'M':
    
    result = formula_de_hb_m(info[2], info[4], info[1], info[5])
   
if info[3] == 'F':
    
    result = formula_de_hb_f(info[2], info[4], info[1], info[5])

print('KCALORIAS QUE DEVERIA CONSUMIR POR DIA:', int(result), 'kcal')
    

