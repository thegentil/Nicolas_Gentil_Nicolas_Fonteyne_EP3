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

info = u[1].strip().split(",")    #Fazendo com que as palavras de uma linha fiquem em linhas separadas na vírgula

#Nomeando as categorias das info:

for e in info:
    if e == info[0]:
        print('Nome:', info[0])
    if e == info[1]:
        print('Idade:', info[1])
    if e == info[2]:
        print('Peso:', info[2])         
    if e == info[3]:
        print('Sexo:', info[3])
    if e == info[4]:
        print('Altura:', info[4])
    if e == info[5]:
        print('Nível de atividade física:', info[5])
print('')

#Criando uma timeline de alimentos ingeridos pelo usuário

lista = []

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

#Adicionando os elementos ao dic_gramas:

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

#Fazendo com que os elementos numéricos da lista info passem para o formato float:

info [1] = float(info[1])
info [2] = float(info[2])         
info [4] = float(info[4])

#Calculando o BMI:

BMI = formula_BMI(info[2], info[4])

if BMI < 18.5:
    
    print('Você é magro demais')
    print('')
    
if BMI >= 18.5:    
    if BMI < 25:        
        print('Você é uma pessoa saudável!')
        print('')
        
if BMI >= 25:
    if BMI < 30:
        print('Você está um pouco acima do peso')
        print('')
        
if BMI >= 30:
    
    print('Você é obeso')
    print('')

#Calorias que deveria consumir:

if info[3] == 'M':
    
    result = formula_de_hb_m(info[2], info[4], info[1], info[5])
   
if info[3] == 'F':
    
    result = formula_de_hb_f(info[2], info[4], info[1], info[5])

print('KCALORIAS QUE DEVERIA CONSUMIR POR DIA:', int(result), 'kcal')
print('')

#Calculando as colrias que ingeriu a mais/menos por dia:
    
for e in dic_dias:

    DeltaKcal = (dic_dias[e][0]) - result
    
    print('No dia',e, ':')    
    
    if DeltaKcal < 0:
        
        print('Você consumiu', int((DeltaKcal**2)**(1/2)), 'kcal a menos do que o recomendado')
        print('')
        
    elif DeltaKcal == 0:
        
        print('Você consumiu o número exato de calorias recomendadas')
        print('')
    
    else: 
    
        print('Você consumiu', int(DeltaKcal), 'kcal a mais do que o recomendado')
        print('')

'''
CRIANDO OS GRÁFICOS
'''
dias = sorted(dic_dias.keys())

dias_plot = list(range(1,len(dias)+1))

resultList = [result]*len(dias)

kcalList = []
protList = []
carbList = []
gordList = []

for e in dias:
    
    kcalList.append(dic_dias[e][0])
    protList.append(dic_dias[e][1])
    carbList.append(dic_dias[e][2])
    gordList.append(dic_dias[e][3])

#Gráfico das calorias consumidas e que deveria consumir:

plt.plot(dias_plot, resultList) #calorias que deveria consumir
plt.plot(dias_plot, kcalList, 'ro') #calorias consumidas
plt.axis(1, 5, 0, 2000)
plt.ylabel('Kcal ideais/Dia')
plt.xlabel('Dias')
plt.title('Calorias consumidas')
plt.show()

#Gráfico das proteínas, carboidratos e gorduras que consumiu:

plt.plot(dias_plot, protList) #pronteínas consumidas
plt.plot(dias_plot, carbList) #carboidratos consumidos
plt.plot(dias_plot, gordList) #gorduras consumidas
plt.axis(1, 5, 0, 200)
plt.ylabel('Kcal ideais/Dia')
plt.xlabel('Dias')
plt.title('Calorias consumidas')
plt.show()