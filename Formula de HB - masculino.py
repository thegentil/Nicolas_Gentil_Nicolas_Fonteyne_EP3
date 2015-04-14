# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:10:45 2015

@author: Nicolas Gentil e Nicolas Fonteyne

Fórmula de Harris-Benedict para o sexo masculino

"""

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
        
              