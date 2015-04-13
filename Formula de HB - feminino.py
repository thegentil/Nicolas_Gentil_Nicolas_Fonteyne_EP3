# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:15:10 2015

@author: Nicolas Gentil e Nicolas Fonteyne

Fórmula de Harris-Benedict para o sexo feminino

"""

def formula_de_hb_f(peso, altura, idade, grau_de_atividade):
    
    if grau_de_atividade == 'minimo':
        
        (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.2
        
    if grau_de_atividade == 'baixo':
        
        (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.375
        
    if grau_de_atividade == 'medio':
        
        (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.55
        
    if grau_de_atividade == 'alto':
        
        (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.725
        
    if grau_de_atividade == 'muito alto':
        
        (447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)) * 1.9  