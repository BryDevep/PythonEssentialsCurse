# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:33:06 2022

@author: riverab
"""

# 1 milla americana = 1609.344 metros;
# 1 galón americano = 3.785411784 litros.

def litr100kmAmillasgal(litros):
    gal=(litros/3.785411784)
    km=100000
    mi=km/1609.344
    return(mi/gal)
    
print(litr100kmAmillasgal(3.9))
 
print(litr100kmAmillasgal(7.5))
    
print(litr100kmAmillasgal(10))

def millasgalAlitr100km(millas):
    metros=millas*1609.344
    



    
    
