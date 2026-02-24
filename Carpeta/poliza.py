#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 00:52:10 2026

@author: Gutierrez Yuridia
"""
#Aqui, probaremos algunas clases que componen a un seguro de autos

class SeguroAuto:
    #este es el metodo constructor que inicializa a los atributos de la clase
    
    def __init__ (self, prima_inicial):
        self.costo_poliza = prima_inicial
        self.cobertura = "10000"
        
    #tipo de cbertura de la poliza
    def definir_cobertura (self, tipo):
        self.cobertura = tipo
        
    #aquí será para aplicar los cargos por lagun siniestro
    def aplicar_cargo(self, monto):
        self.costo_poliza =self.costo_poliza + monto
        
    #aqui el metodo para aplicar descentos al cliente
    def aplicar_descuento(self, monto):
        self.costo_poliza = self.costo_poliza - monto
        
#%%
# menu_seguros.py
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
    