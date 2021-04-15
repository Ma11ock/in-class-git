#!/usr/bin/env python



def calc(a, b):
    sum = a + b
    divid = a / b
    mult = a * b
    lesser = a - b
    modulo = a % b

    myList = [ sum, divid, lesser, modulo ]
    print(myList)
    
    
    
calc(3, 4)    
