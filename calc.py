#!/usr/bin/env python



def calc(a, b):
    sum = a + b
    divid = a / b
    mult = a * b
    lesser = a - b
    modulo = a % b

    myList = [ sum, divid, lesser, modulo, mult ]
    listSum = 0
    for i in myList:
        listSum += i
    print(listSum)    
    print(myList)
    
    
    
calc(3, 4)    
