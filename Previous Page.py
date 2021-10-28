# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:39:32 2021

@author: okanr
"""

class Previous:
    
    def PreviousAdmin():
        
        flag = True
        
        while flag:
            
                print('Previous')
                print('**********Admin Panel***********')
                print('----------------------------------')
                print('1: Add Staff')
                print('2: Delete Staff')
                print('3: Add Member')
                print('4: Delete Member')
                print('5: Add Product')
                print('6: Delete Product')
                print('7: Display the Staffs')
                print('8: Display the Members')
                print('9: Display the Products')
                print('10: Search the staff informations with ID No')
                print('11: Search the member informations with ID No')
                print('12: Search the product informations with ID No')
                print('13: Sell Products')
                print('14: Add New Products over existing ones.')
                print('15: Calculator')
                print('q: Quit')
                
                press2 = input('Choose please: ')
                
                if press2 == '1':
                
                    AdminPage.insertStaff()
                
                elif press2 == '2':
                
                    AdminPage.deleteStaff()
                
                elif press2 == '3':
                
                    AdminPage3member.insertMembers()
                
                elif press2 == '4':
                
                    AdminPage3member.deleteMembersDictionary()
                
                elif press2 == '5':
                
                    AdminPage2Products.insertProducts()
                
                elif press2 == '6':
                
                    AdminPage2Products.deleteProductsDict()
                
                elif press2 == '7':
                
                    AdminPage.displayDictt()
                
                elif press2 == '8':
                
                    AdminPage3member.displayAllMembersWithDict()
                
                elif press2 == '9':
                
                    AdminPage2Products.displayDict()
                
                elif press2 == '10':
                
                    AdminPage.searchWithIDno()
                
                elif press2 == '11':
                
                    AdminPage3member.searchWithIDno()
                
                elif press2 == '12':
                
                    AdminPage2Products.searchWithIDnoProducts()
                
                elif press2 == '13':
                
                    AdminPage2Products.sellProduct()
                
                elif press2 == '14':
                
                    AdminPage2Products.insertNewProductsUponExistingOnes()
                    
                elif press2 == '15':
                    
                    AdminPage2Products.useCalculator()
                
                elif press2 == 'q':
                    
                    print('Logout')
                    flag = False

    def PreviousCashier():
        
        flag1 = True
        
        while flag1:
        
        
        
                print('*********Cashier Panel**********')
                print('----------------------------------')
                print('1: Add Member')
                print('2: Delete Member')
                print('3: Add Product')
                print('4: Delete Product')
                print('5: Display the Members')
                print('6: Display the Products')
                print('7: Search the member informations with ID No')
                print('8: Search the product informations with ID No')
                print('9: Sell Products')
                print('10: Add Products over existing ones.')
                print('11: Calculator')
                print('q: Quit')
                
                press3 = input('Choose please: ')
                
                if press3 == '1':
                
                    CashierPage.insertMemberss()
                
                elif press3 == '2':
                
                    CashierPage.deleteMembersDictionaryy()
                
                elif press3 == '3':
                
                    CashierPage.insertProductss()
                
                elif press3 == '4':
                
                    CashierPage.deleteProductsDictt()
                
                elif press3 == '5':
                
                    CashierPage.displayAllMembersWithDictt()
                
                elif press3 == '6':
                
                    CashierPage.displayDictt()
                
                elif press3 == '7':
                
                    CashierPage.searchWithIDnoo()
                
                elif press3 == '8':
                
                    CashierPage.searchWithIDnoProductss()
                
                elif press3 == '9':
                
                    CashierPage.sellProductt()
                
                elif press3 == '10':
                
                    CashierPage.insertNewProductsUponExistingOness()
                
                elif press3 == '11':
                    
                    CashierPage.useCalculator()
            
                elif press3 == 'q':
                    
                    print('Logout.')
                    flag1 = False
        
        
    
    
    
    def previousMember():
        
                print('***********Member Panel***********')
                print('------------------------------------')
                print('1: Display the Products')
                print('2: Search the product informations with ID No')
                print('q: Quit')
                
                press4 = input('Choose please: ')
                
                if press4 == '1':
                
                    Member.displayDict()
                
                elif press4 == '2':
                
                    Member.searchWithIDnoProducts()
                
                elif press4 == 'q':
                    
                    print('Logout.')
                    flag = False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        