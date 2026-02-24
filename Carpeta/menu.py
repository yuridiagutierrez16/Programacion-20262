#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:42:19 2026

@author: programacion
"""

# menu_seguros.py
# from poliza import *
class Menu:
    pass
    print("Emision de la poliza")
    mi_seguro = SeguroAuto(5000)
    print(mi_seguro.costo_poliza)
    
    print("Tipo de cobertura que abarca su seguro de Auto")
    mi_seguro.definir_cobertura("Amplias")
    print(mi_seguro.cobertura)
    
    print("Por siniestro,subimos el costo") #cargo
    mi_seguro.aplicar_cargo(1500)
    print ("Aplicando recargo por siniestro...")
    print ("Nuevo costo")
    print (mi_seguro.costo_poliza)
    
    #descuento por buen conductor. suponiendo que el cliente tomó un curso 
    #de manejo
    mi_seguro.aplicar_descuento(300)
    print("Aplicando el descuento por curso...")
    print("Costo final de la poliza")
    print (mi_seguro.costo_poliza)
    