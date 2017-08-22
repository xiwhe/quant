#!/bin/python
# -*- coding:utf-8 -*-
import time
import price as prc
import tushare as ts
import storage as sv

all_stocks = ts.get_day_all()

print("get data done")
sv.saveData(all_stocks)
print(all_stocks)
# all_stocks=pd.read_json(sv.readData(), convert_axes=False, convert_dates=False)

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))

start = time.time()

for index in all_stocks.index:
    stock_code = all_stocks.code[index]

    if all_stocks.abvalues[index] > 50:
        continue
    if not prc.istradeable(all_stocks.high[index], all_stocks.low[index]):
        continue
    if all_stocks.volratio[index] < 1.5:
        continue
    if not all_stocks.preprice[index] < all_stocks.price[index] < all_stocks.preprice[index] * 1.05:
        continue

    print('Get it! code ', stock_code)

end = time.time()
print(f"mission complete {end-start:f} sec used")
