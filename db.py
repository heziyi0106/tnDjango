# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:57:03 2023

@author: user
"""

#將flask和mysql連接
import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1',user='tngood',password='987654321',database='tndjango',auth_plugin='mysql_native_password')
#auth_plugin 編碼

cursor = conn.cursor() 

