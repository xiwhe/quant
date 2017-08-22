# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:19:36 2016

@author: SNoW
"""
import time
import tushare as ts
"""
stockDataList = []

def saveData(stockData):
    stockDataList.insert(stockData)

def showData():
    print stockDataList
"""

projectDir="./"
time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
dataFile=projectDir + "stockData" + time + ".json"

#print dataFile

def saveData( stockData ):
    stockData.to_json(dataFile,orient='records')

def readData():
 #   stockData.read_json()
 #   return json
    return 
