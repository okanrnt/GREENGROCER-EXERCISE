# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:30:55 2021

@author: okanr_000
"""

class Password:
    
    def forgotPassword():
        
        flag = True
        
        while flag:
            
            yetki = input('Member:  1, Staff: 2: ')
            
            if yetki == '1':
                
                ID = input('ID no: ')
                name = input('Enter your name: ')
                surname = input('Enter your surname: ')

                sample3 = AdminPage.staffDict[ID]
                sample3.pop('password')
                newPassword = input('Enter new password: ')
                newRepassword = input('Re-enter the new password: ')
                if newPassword == newRepassword:
                    sample3['password'] = newPassword
                else:
                    print('Passwords do not match.')
                    newRepassword = input('Re-enter the new password: ')
                    sample3['password'] = newPassword
            
                flag = False
            
            elif yetki == '2':
                
                ID = input('ID no: ')
                name = input('Enter your name: ')
                surname = input('Enter your surname: ')
                    
                sample4 = AdminPage3member.memberDict[ID]
                sample4.pop('password')
                newPassword = input('Enter new password: ')
                newRepassword = input('Re-enter the new password: ')
                if newPassword == newRepassword:
                    sample4['password'] = newPassword
                else:
                    print('Passwords do not match.')
                    newRepassword = input('Re-enter the new password: ')
                    sample4['password'] = newPassword
                
                flag = False
            
            else:
                
                print('Make a valid key.')
            
            
            
            
            
            
            
            