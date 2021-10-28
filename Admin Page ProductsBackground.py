# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:38:51 2021

@author: okanr_000
"""


class AdminPage2Products:
    
    
    
    productsDict = dict()
    productsList = list()
    
    def __init__(self,ID,barcodeCode,name,group,weight,price,endorsement):
        
        self.ID = ID
        self.barcodeCode = barcodeCode
        self.name = name
        self.group = group
        self.weight = weight
        self.price = price
        self.endorsement = endorsement
        self.insertProductsDictionary()
        self.listProductsID()
        
    def insertProductsDictionary(self):
        
        AdminPage2Products.productsDict.update({
            self.ID : {
                'Barcode Code' : self.barcodeCode,
                'Name' : self.name,
                'Group' : self.group,
                'Weight' : self.weight,
                'Price' : self.price,
                'Endorsement' : self.endorsement
                }
            })
        
    
    def searchWithIDnoProducts():
        ID = input('ID no: ')
        for k,v in AdminPage2Products.productsDict[ID].items():
            print(' {} : {}'.format(k,v))
        Previo.proWhile()
    
        
    def listProductsID(self):
        
        AdminPage2Products.productsList.append(self.ID)
        
    def deleteProductsDict():
        
        ID = input('ID: ')
        if ID in  AdminPage2Products.productsList:
             AdminPage2Products.productsList.remove(ID)
             AdminPage2Products.productsDict.pop(ID)
             
        else:
            print('The ID does not exist.')
        Previo.proWhile()
    
    def displayDict():
        
        for k,v in AdminPage2Products.productsDict.items():
            print(' {} : {}'.format(k,v))
        Previo.proWhile()
        
    def insertProducts():
        import mysimplemodule as mys
        
        for j in range(int(input('How many products type you want to add: '))):
        
            if len(AdminPage2Products.productsList) == 0:
                ID = '1'
            else:
                ID = str(int(AdminPage2Products.productsList[-1]) +1)
            barcodeCode = mys.barcodeCodeF()
            name = input('Name: ')
            group = input('Group: ')
            weight = input('Kilo: ')
            price = input('Price: ')
            endorsement = str(int(price) * int(weight))
            
            
            AdminPage2Products(ID,barcodeCode,name,group,weight,price,endorsement)
        Previo.proWhile()
      
    def sellProduct():
        
        soldID = input('Product ID no: ')
        soldProduct = input('Name of the product sold: ')
        soldWeight = int(input('kilo: '))
        
        
        sold = AdminPage2Products.productsDict[soldID]
        
        trying = sold['Weight']
        new_weight = int(trying) - soldWeight
        price = sold['Price']
        endor = sold['Endorsement']
        new_endorsement = int(endor) - (soldWeight * int(price))
        for v in sold.values():
            if v == soldProduct:
                sold.pop('Weight')
                sold.pop('Endorsement')
                sold['Weight'] = str(new_weight)
                sold['Endorsement'] = str(new_endorsement)
        Previo.proWhile()
                
    def insertNewProductsUponExistingOnes():
        
        loadedID = input('Ürünün ID no: ')
        loadedProduct = input('Product Name: ')
        loadedWeight = int(input('Kilo:  '))
        newPrice = int(input('New Price: '))
        
        loaded = AdminPage2Products.productsDict[loadedID]
        newV = loaded['Weight']
        new_weight = int(newV) + loadedWeight
        newE = loaded['Endorsement']
        new_endorsement = new_weight * newPrice
        
        for value in loaded.values():
            
            if value == loadedProduct:
                loaded.pop('Weight')
                loaded.pop('Endorsement')
                loaded.pop('Price')
                loaded['Price'] = str(newPrice)
                loaded['Weight'] = str(new_weight)
                loaded['Endorsement'] = str(new_endorsement)
        
        Previo.proWhile()
    
    def useCalculator():
        
        process = input('+: sum\n-: subtract\n*: multiplication\n/: divide\nChoose:')
        Previo.calculatorfunc(process)
        Previo.proWhile()
        
        
        
        
    
        
    
        