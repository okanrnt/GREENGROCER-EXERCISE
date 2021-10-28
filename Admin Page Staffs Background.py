# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:17:05 2021

@author: okanr_000
"""

class AdminPage:
    
    ID = '999'
    name = 'admin'
    surname = 'admin'
    password = '1'
    staffDict = {}
    staffList = []

    def __init__(self, ID, name, surname, password, repassword, dateOfBirth):

        self.ID = ID
        self.name = name
        self.surname = surname
        self.password = password
        self.repassword = repassword
        self.dateOfBirth = dateOfBirth
        self.insertDictio()
        self.apppendList()

    def insertDictio(self):

        AdminPage.staffDict.update({
            self.ID: {
                'name': self.name,
                'surname': self.surname,
                'password': self.password,
                'dateOfBirth': self.dateOfBirth
            }
        })

    def apppendList(self):

        AdminPage.staffList.append(self.ID)

    def displayDictt():

        for k,v in AdminPage.staffDict.items():
            print(' {} : {}'.format(k,v))
        
        while True:
            pressP = input('Press to p for to come back.')
            if pressP == 'p':
                Previous.PreviousAdmin()
                break
            else:
                print('Wrong key.')
        
                
       
    def searchWithIDno():

        IDno = input('ID no: ')
        for k,v in AdminPage.staffDict[IDno].items():
            print(' {} : {}'.format(k,v))
        Previo.proWhile()

    def insertStaff():

        for i in range(int(input('How many staffs you want to add: '))):

            if len(AdminPage.staffList) == 0:
                ID = '1'
            else:
                ID = str(int(AdminPage.staffList[-1]) + 1)
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
            
            print('Staff added. ID no: {}'.format(ID))
             
            AdminPage(ID, name, surname, password, repassword, dateOfBirth)
            
        Previo.proWhile()

    def deleteStaff():

        IDno = input('ID no: ')
        if IDno in AdminPage.staffList:
            AdminPage.staffList.remove(IDno)
            AdminPage.staffDict.pop(IDno)
            print('The staff deleted.')
        else:
            print('The staff not found.')

        Previo.proWhile()



