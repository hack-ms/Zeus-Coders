#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyodbc

def GetRowsFromDB(sqlConfig, path):
    conn = pyodbc.connect(sqlConfig)
    cursor = conn.cursor()
    data_file = open(path)
    sqlText = data_file.read()
    cursor.execute(sqlText)

    listProp = []
    for row in cursor:
        listProp.append(row)
    
    return listProp