# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:19:29 2015

@author: Nícolas Fonteyne e Nícolas Gentil

formulas utilizadas

"""

def regra_de_tres (gramas_ingeridas, kcal_por_100g, prot_por_100g, carb_por_100g, gord_por_100g  ):
    return (gramas_ingeridas/100)*kcal_por_100g
    return (gramas_ingeridas/100)*prot_por_100g
    return (gramas_ingeridas/100)*carb_por_100g
    return (gramas_ingeridas/100)*gord_por_100g
    
    

def formula_de_hb_f(peso, altura, idade, grau_de_atividade):
    
    if grau_de_atividade == 'minimo':
        
        return (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.2
        
    if grau_de_atividade == 'baixo':
        
        return (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.375
        
    if grau_de_atividade == 'medio':
        
        return (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.55
        
    if grau_de_atividade == 'alto':
        
        return (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.725
        
    if grau_de_atividade == 'muito alto':
        
        return (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.9  
        
        
        
def formula_de_hb_m(peso, altura, idade, grau_de_atividade):

    if grau_de_atividade == 'minimo':
        
        return (88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.2
        
    if grau_de_atividade == 'baixo':
        
        return (88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.375
        
    if grau_de_atividade == 'medio':
        
        return (88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.55
        
    if grau_de_atividade == 'alto':
        
        return (88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.725
        
    if grau_de_atividade == 'muito alto':
        
        return (88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)) * 1.9  
 
