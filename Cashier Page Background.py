# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:17:07 2021

@author: okanr_000
"""

class CashierPage:
    
    def searchWithIDnoProductss():
        
        ID = input('ID no: ')
        for k,v in AdminPage2Products.productsDict[ID].items():
            print(' {} : {}'.format(k,v))
        
        Previo.preWhile()
        
    
    def deleteProductsDictt():
        
        ID = input('ID: ')
        if ID in  AdminPage2Products.productsList:
             AdminPage2Products.productsList.remove(ID)
             AdminPage2Products.productsDict.pop(ID)
             print('The product deleted.')
             
        else:
            print('The ID does not exist.')
        Previo.preWhile()
    
    def displayDictt():
        
        for k,v in AdminPage2Products.productsDict.items():
            print(' {} : {}'.format(k,v))
        Previo.preWhile()
        
    def insertProductss():
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
        Previo.preWhile()
      
    def sellProductt():
        
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
                print('Selling is successful.')
        Previo.preWhile()
                
    def insertNewProductsUponExistingOness():
        
        loadedID = input('The product ID no: ')
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
                print('The products updated.')
        
        Previo.preWhile()
        
    def deleteMembersDictionaryy():
        
        ID = input('ID: ')
        if ID in AdminPage3member.memberList:
            AdminPage3member.memberDict.pop(ID)
            AdminPage3member.memberList.remove(ID)
            print('The member deleted')
        else:
            print('The member not found.')
        Previo.preWhile()
        
    def searchWithIDnoo():
        
        IDno = input('ID no: ')
        for k,v in AdminPage3member.memberDict[IDno].items():
            print(' {} : {}'.format(k,v))
        Previo.preWhile()
        
    def displayAllMembersWithDictt():
         
        for k,v in AdminPage3member.memberDict.items():
            print(' {} : {}'.format(k,v))
        Previo.preWhile()
        
        
    def insertMemberss():
        
        for i in range(int(input('How many members you want to add: '))):
        
            
            if len(AdminPage3member.memberList) == 0:
                ID = '1'
            else:
                ID = str(int(AdminPage3member.memberList[-1]) + 1)
            name = input('Name: ')
            surname = input('Surname: ')
            password = input('Password: ')
            repassword = input('Repassword: ')
            if password == repassword:
                print('Passwords match.')
            else:
                print('Passwords do not match.')
                repassword = input('Repassword: ')
            dateOfBirth = input('dateOfBirth: ')
            print('The member added. ID no: {}'.format(ID))
        
            AdminPage3member(ID,name,surname,password,repassword,dateOfBirth)
        
        Previo.preWhile()
    
    def useCalculator():
        
        process = input('+: sum\n-: subtract\n*: multiplication\n/: divide\nChoose:')
        Previo.calculatorfunc(process)
        Previo.preWhile()
    

    
    
    
    
    
    