# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:59:06 2022

@author: riverab
"""

def funlist(lista):
    for item in lista:
        print("Hola", item)
    print("")
    
funlist(["Ana"])
funlist(["Ana", "Juan"])
funlist(["Ana", "Juan", "Lucas"])


def createList(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return(myList)

print(createList(10))
