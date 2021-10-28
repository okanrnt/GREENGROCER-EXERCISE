# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:01:06 2021

@author: okanr_000
"""

def barcodeCodeF():   #Module Func
    import random
    barcodeList = []
    barcodeCode = random.randint(100000, 999999)
    if barcodeCode in barcodeList:
        barcodeCode = random.randint(100000, 999999)
    else:
        barcodeList.append(barcodeCode)
        return barcodeCode

    

