# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:39:20 2021

@author: okanr_000
"""

class AdminPage3member:
    
    
    memberDict = {}
    memberList = list()
    
    def __init__(self,ID,name,surname,password,repassword,dateOfBirth):
        
        self.ID = ID
        self.name = name
        self.surname = surname
        self.password = password
        self.repassword = repassword
        self.dateOfBirth = dateOfBirth
        self.insertMembersDictionarty()
        self.listMembersID()
    
    def insertMembersDictionarty(self):
        
        AdminPage3member.memberDict.update({
            self.ID: {
                'name': self.name,
                'surname' : self.surname,
                'password' : self.password,
                'dateOfBirth' : self.dateOfBirth
                }
            })
        
        
    def listMembersID(self):
        
        AdminPage3member.memberList.append(self.ID)
    
    def deleteMembersDictionary():
        
        ID = input('ID: ')
        if ID in AdminPage3member.memberList:
            AdminPage3member.memberDict.pop(ID)
            AdminPage3member.memberList.remove(ID)
        else:
            print('No member found with this ID number.')
        Previo.proWhile()
        
    def searchWithIDno():
        
        IDno = input('ID no: ')
        for k,v in AdminPage3member.memberDict[IDno].items():
            print(' {} : {}'.format(k,v))
        Previo.proWhile()
        
    def displayAllMembersWithDict():
         
        print(AdminPage3member.memberDict)
        Previo.proWhile()
        
        
    def insertMembers():
        
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
            dateOfBirth = input('DateTime: ')
            print('The member added. ID no: {}'.format(ID))
        
            AdminPage3member(ID,name,surname,password,repassword,dateOfBirth)
        
        Previo.proWhile()
  

AdminPage3member('1','okan', 'öztan', '1234', '1234', '20.08.1990')
AdminPage3member('2','Furkan', 'Öztan', '5896', '5896', '17.03.1999')








