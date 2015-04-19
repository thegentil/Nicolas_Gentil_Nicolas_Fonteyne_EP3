# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:57:23 2015

@author: Nicolas Gentil e Nicolas Fonteyne

Projeto 3

"""

from formulas_utilizadas import *
import matplotlib.pyplot as plt


'''
Abrindo e lendo os arquivos
'''

alimentos = open('alimentos.csv', encoding="latin1")          #Abrindo a lista de alimentos
usuario = open('usuario.csv',encoding="latin1")          #Abrindo a lista do usuário

a = alimentos.readlines()          #Lendo a lista de alimentos
u = usuario.readlines()          #Lendo a lista do usuário

'''
Criando os dicionários
'''

dic_al = {}  
dic_gramas = {}
dic_dias = {}
dic_consumo = {}

'''
Organizando a lista do usuário
'''

info = u[1].strip().split(",")          #Fazendo com que as palavras de uma linha fiquem em linhas separadas na vírgula

lista = []

#Criando uma timeline de alimentos ingeridos pelo usuário

for l in u[3:]:

    b = l.strip().split(",") 
    lista.append(b)

lista = sorted(lista)

'''
Organizando a lista de alimentos

Pedaço: 

1 = gramas
2 = kcalorias
3 = proteínas
4 = carboidratos
5 = gorduras
'''

#Adicionando os elementos no dic_al:

for e in a[1:]:
    pedacos = e.strip().split(",")
    dic_al[pedacos[0]] = [float(pedacos[1]), float(pedacos[2]), float(pedacos[3]), float(pedacos[4]), float(pedacos[5])]

'''
Criando o programa que irá relacionar os valores aos dias
'''

#adicionando os elementos ao dic_gramas:

for e in lista:
    
    dic_gramas[e[1]] = e[2]
    
for e in dic_gramas:
    
    dic_gramas[e] = float(dic_gramas[e])

#Adicionando os elementos ao dic_dias:

listavalues = []

for i in range(len(lista)):
    
    dic_dias[lista[i][0]] = listavalues
    
    if lista[i][0] != lista[0][0]: 
        
        if lista[i][0] == lista[i-1][0]:
            listavalues.append(lista[i][1])
        else:
            listavalues = [lista[i][1]]
    else:
        listavalues.append(lista[i][1])
        
#Substituindo valores de gramas em dic_al pelos valores em gramas de dic_gramas

for e in dic_gramas:
    
    dic_al[e][0] = dic_gramas[e]

#Calculando a ingestão de kcal, carb, prot e gord por alimento consumido e adicionando os valores obtidos em dic_consumo
    
for e in dic_al:
    
    if e in dic_gramas:
    
        x = regra_de_tres (dic_al[e][0], dic_al[e][1], dic_al[e][2], dic_al[e][3], dic_al[e][4])

        dic_consumo[e] = x

#Substituindo os valores do dic_dias pelos valores de dic_consumo:

for e in dic_dias:  
    
    for i in range(len(dic_dias[e])):
            
        c = dic_dias[e][i]
            
        for w in dic_consumo:
            
            if w in dic_dias[e]:
                
                dic_dias[e].append(dic_consumo[w])
                
                dic_dias[e].remove(w)
               
#Somando os elementos das listas que compõem os valores das chaves do dic_dias:

for e in dic_dias:
    
    Lkcal_consumidas = []
    Lprot_consumidas = []
    Lcarb_consumidos = []
    Lgord_consumidas = []
    
    for w in dic_dias[e]:
                
       Lkcal_consumidas.append(w[0]) 
       Lprot_consumidas.append(w[1])
       Lcarb_consumidos.append(w[2])
       Lgord_consumidas.append(w[3])
    
    Rkcal = int(sum(Lkcal_consumidas))
    Rprot = int(sum(Lprot_consumidas))
    Rcarb = int(sum(Lcarb_consumidos))
    Rgord = int(sum(Lgord_consumidas))
    
    dic_dias[e] = [Rkcal, Rprot, Rcarb, Rgord]

print(dic_dias)
'''
Determinando o número de calorias que o usuário deveria ingerir a cada dia
''' 

#Fazendo com que os elementos numéricos da lista info passem para o formato float

info [1] = float(info[1])
info [2] = float(info[2])         
info [4] = float(info[4])

# calorias que deveria consumir:

if info[3] == 'M':
    
    result = formula_de_hb_m(info[2], info[4], info[1], info[5])
   
if info[3] == 'F':
    
    result = formula_de_hb_f(info[2], info[4], info[1], info[5])

print('')
print('KCALORIAS QUE DEVERIA CONSUMIR POR DIA:', int(result), 'kcal')


'''
Criando os gráficos
'''

dias = [0, 1, 2, 3, 4]

plt.plot(dias, result)
plt.axis(0, 5, 0, 3000)
plt.ylabel('Kcal ideais/Dia')
plt.xlabel('Dias')
plt.title('Calorias consumidas')
plt.show()

plt.plot(dias, result)
plt.axis(0, 5, 0, 3000)
plt.ylabel('Kcal ideais/Dia')
plt.xlabel('Dias')
plt.title('Calorias consumidas')
plt.show()
    

