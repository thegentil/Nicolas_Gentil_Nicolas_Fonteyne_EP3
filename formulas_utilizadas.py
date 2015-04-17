# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:19:29 2015

@author: Nícolas Fonteyne e Nícolas Gentil

formulas utilizadas

"""

import doctest


def regra_de_tres (gramas_ingeridas, kcal_por_100g, prot_por_100g, carb_por_100g, gord_por_100g):
    
    '''
    calcula o equivalente de kcal, prot, gord, carb para a quant de gramas ingeridas pelo usuário
    >>> regra_de_tres(50, 200, 10, 10, 10)
    [100.0, 5.0, 5.0, 5.0]
    '''

    listaA= [0]*4

    listaA[0] = round((gramas_ingeridas/100)*kcal_por_100g, 3)
    listaA[1] = round((gramas_ingeridas/100)*prot_por_100g, 3)
    listaA[2] = round((gramas_ingeridas/100)*carb_por_100g, 3)
    listaA[3] = round((gramas_ingeridas/100)*gord_por_100g, 3)

    print( listaA)
    

def formula_de_hb_f(peso, altura, idade, grau_de_atividade):
    
    '''
    calcula o número de calorias que devem ser consumidas (p/ mulheres)
    >>> formula_de_hb_f(50, 150, 20, 'alto')
    2219.385
    '''
    
    if grau_de_atividade == 'minimo':
        
        return round((447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.2, 3)
        
    if grau_de_atividade == 'baixo':
        
        return round((447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.375, 3)
        
    if grau_de_atividade == 'medio':
        
        return round((447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.55, 3)
        
    if grau_de_atividade == 'alto':
        
        return round((447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.725, 3)
        
    if grau_de_atividade == 'muito alto':
        
        return round((447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.9, 3)  
        
        
        
def formula_de_hb_m(peso, altura, idade, grau_de_atividade):
    
    '''
    calcula o número de calorias que devem ser consumidas (p/ homens)
    >>> formula_de_hb_m(50, 150, 20, 'alto')
    2353.521
    '''

    if grau_de_atividade == 'minimo':
        
        return round((88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.2, 3)
        
    if grau_de_atividade == 'baixo':
        
        return round((88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.375, 3)
        
    if grau_de_atividade == 'medio':
        
        return round((88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.55, 3)
        
    if grau_de_atividade == 'alto':
        
        return round((88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.725, 3)
        
    if grau_de_atividade == 'muito alto':
        
        return round((88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.9, 3)
        
        
def formula_BMI(peso, altura):
    
    '''
    calcula a fórmula de Nick Trefethen
    >>> formula_BMI(85, 1.85)
    23.737
    '''
    
    bmi = round(1.3*peso/altura**2.5, 3)  

    return bmi     

    
if __name__=="__main__":
    doctest.testmod(verbose="True")    
 
