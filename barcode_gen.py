# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:44:57 2022

@author: ekanem007
"""
#code requirment: the barcode package must be installed in your python terminal

#import barcode package
import barcode
#enter the thirteen digit to encoded in the " " below. Note: digits below must be up to 13 for code to work.
bar=barcode.get("ean13","0980000000000")
#enter the file path to the desired storage location for the barcode in the (bracket) below 
bar.save("C:/Users/admin/folder/name")
#Note barcode image will be saved in svg format.

#Happy Coding ('_')