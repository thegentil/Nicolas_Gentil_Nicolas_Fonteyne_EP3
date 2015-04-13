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

partes = u[1].strip().split(",")          #Fazendo com que as palavras de uma linha fiquem em linhas separadas

for p in partes:
    print(p)
        
print('')

for l in u[3:]:          #Criando uma timeline de alimentos ingeridos pelo usuário
    for pedaço in l.strip().split(","):
        print(pedaço)


