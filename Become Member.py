# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:17:08 2021

@author: okanr_000
"""

class BecomeMember:
    
    def beMember():
        
            
        if len(AdminPage3member.memberList) == 0:
            ID = '1'
        else:
            ID = str(int(AdminPage3member.memberList[-1]) + 1)
        name = input('Name: ')
        surname = input('Surname: ')
        password = input('Password: ')
        while True:
            repassword = input('Repassword: ')
            if password == repassword:
                print('Passwords match.')
                break
            else:
                print('Passwords do not match.')
        dateOfBirth = input('dateOfBirth: ')
        print('The operation is successful. ID no: {}'.format(ID))
        
        AdminPage3member(ID,name,surname,password,repassword,dateOfBirth)
        


     
        
     
        