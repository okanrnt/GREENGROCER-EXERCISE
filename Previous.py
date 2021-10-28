# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 22:23:43 2021

@author: okanr
"""

class Previo:
    
    def proWhile():
        
        while True:
            
            pressP = input('Press to p to come back: ')
            if pressP == 'p':
                Previous.PreviousAdmin()
                break
            else:
                print('Wrong key.')
                
    def preWhile():
        
        while True:
            pressC = input('Press to p to come back: ')
            if pressC == 'p':
                Previous.PreviousCashier()
                break
            else:
                print('Wrong key.')
                
    def pretrywhile():
        
         while True:
            pressM = input('Press to p to come back: ')
            if pressM == 'p':
                Previous.previousMember()
                break
            else:
                print('Wrong key.')
    
            
  
    def calculatorfunc(process):
        def sum_():
            while True:
                a = input('Kilo: ')
                b = input('Price: ')
                try:
                    x = int(a)
                    y = int(b)
                    print(x+y)
                    break
                except ValueError:
                    print('You can enter just a number.')
                
        def subtraction():
            while True:
                a = input('Kilo: ')
                b = input('Price: ')
                try:
                    x = int(a)
                    y = int(b)
                    print(x-y)
                    break
                except ValueError:
                    print('You can enter just a number.')
                
        def multiplication():
            while True:
                a = input('Kilo: ')
                b = input('Price: ')
                try:
                    x = int(a)
                    y = int(b)
                    print(x*y)
                    break
                except ValueError:
                    print('You can enter just a number.')
                
        def divide():
           while True:
                a = input('Kilo: ')
                b = input('Price: ')
                try:
                    x = int(a)
                    y = int(b)
                    print(x/y)
                    break
                except ValueError:
                    print('You can enter just a number.')
                except ZeroDivisionError:
                    print('You cannot divide the number to zero.')
                
        if process == '+':
            return sum_()
        elif process == '-':
            return subtraction()
        elif process == '*':
            return multiplication()
        elif process == '/':
            return divide()
        else:
            print('Wrong key.')
            return None
                
        
                
                
                
                
                
                
                
                
                
                
                
                
                
