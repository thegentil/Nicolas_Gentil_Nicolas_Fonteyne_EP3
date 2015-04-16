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

#Criando o dicionário

dic_al = {}  

#Organizando a lista do usuário

info = u[1].strip().split(",")          #Fazendo com que as palavras de uma linha fiquem em linhas separadas na vírgula

for p in info:        
    print(p)
        
print('')

#Criando uma timeline de alimentos ingeridos pelo usuário

lista = []


for l in u[3:]:

    b = l.strip().split(",") 
    lista.append(b)

    for pedaço in b:
        print(pedaço)

for e in sorted(lista):
    data = e[0]
    alimento = e[1]
    gramas = float(e[2])  

#Organizando a lista de alimentos

for e in a[1:]:
    pedacos = e.strip().split(",")
    dic_al[pedacos[0]] = [float(pedacos[1]), float(pedacos[2]), float(pedacos[3]), float(pedacos[4]), float(pedacos[5])]
    #pedaço 1 = gramas / 2 = kcalorias / 3 = proteínas / 4 = carboidratos / 5 = gorduras

#Fazendo com que os elementos numéricos da lista info passem para o formato float

info [1] = float(info[1])
info [2] = float(info[2])         
info [4] = float(info[4])

# calorias, proteínas, carbs e gord consumidas:

print(sorted(lista))

for e in sorted(lista):
    data = e[0]
    alimento = e[1]
    gramas = float(e[2])
    if e != lista[0]:
        if e[0] != e-1[0]:
            kcal_por_100g = dic_al[alimento][1]
            prot_por_100g = dic_al[alimento][2]
            carb_por_100g = dic_al[alimento][3]
            gord_por_100g = dic_al[alimento][4]
        else:
            print('')
            kcal_por_100g = dic_al[alimento][1]
            prot_por_100g = dic_al[alimento][2]
            carb_por_100g = dic_al[alimento][3]
            gord_por_100g = dic_al[alimento][4]
    else:
        kcal_por_100g = dic_al[alimento][1]
        prot_por_100g = dic_al[alimento][2]
        carb_por_100g = dic_al[alimento][3]
        gord_por_100g = dic_al[alimento][4]

    x = regra_de_tres (gramas, kcal_por_100g, prot_por_100g, carb_por_100g, gord_por_100g)
    print(x)

# calorias que deveria consumir:

print('')

if info[3] == 'M':
    
    result = formula_de_hb_m(info[2], info[4], info[1], info[5])
   
if info[3] == 'F':
    
    result = formula_de_hb_f(info[2], info[4], info[1], info[5])

print('KCALORIAS QUE DEVERIA CONSUMIR POR DIA:', int(result), 'kcal')
    

