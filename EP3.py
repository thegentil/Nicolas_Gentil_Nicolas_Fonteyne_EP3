# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:57:23 2015

@author: Nicolas Gentil e Nicolas Fonteyne

Projeto 3

"""

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
    for pedaço in l.strip().split(","):
        print(pedaço)
     
#Criando os dicionários

dic_al = {}     

#Organizando a lista de alimentos

for e in a[1:]:
    pedacos = e.strip().split(",")
    dic_al[pedacos[0]] = [float(pedacos[1]), float(pedacos[2]), float(pedacos[3]), float(pedacos[4]), float(pedacos[5])]

print(dic_al.items())   




         


