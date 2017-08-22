# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:11:49 2016

@author: SNoW
"""

import pandas as pd
debug = False
maxLowPrice = 10

def priceRise(stockData: object, index: object = 0) -> object:
    priceClose = stockData['close']
    
    if ( priceClose[index+1] < priceClose[index] < 1.05*priceClose[index+1] ):
        if debug:
            print('%s breakthrough!!! prc today %f prc yesterday %f prc increase %f' \
                    % (stockData.index[index], \
                    priceClose[index],priceClose[index+1], \
                    priceClose[index]/priceClose[index+1]))
        return True
    else:
#        print volume[index]
        return False


def istradeable(priceHigh, priceLow):

    if (priceHigh == priceLow):
        return False
    else:
        return True

def isLowPrice(stockData, index = 0):
    priceClose = stockData['close']
    if priceClose[index] < maxLowPrice:
        return True
    else:
        return False

#cPrice for close price
def MACD(stockData):
    MACDData = stockData.sort_index()
    cPrice = MACDData.close
    EWMA_zero = cPrice.ewm(span = 13).mean() - cPrice.ewm(span = 13).mean()
#    EWMA_zero.plot()
    EWMA_diff = cPrice.ewm(span = 13).mean() - cPrice.ewm(span = 26).mean()
#    EWMA_diff.plot()
    if( EWMA_diff[EWMA_diff.size -1] >0 ):
        return True
    else:
        return False