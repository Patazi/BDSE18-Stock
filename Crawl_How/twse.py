# -*- coding: UTF-8 -*-
import csv
import pandas as pd
import numpy as np
import json as js 
import requests
import time
import random
from datetime import datetime
from tqdm import trange,tqdm

def Stock_crawl(stockNo,Name):
    
    starttime= datetime.now() #紀錄多久
    dates=[]
    # 獲取今天日期
    now_time = datetime.now().strftime('%Y%m%d')

    # 選擇日期範圍，證交所資料從20100101年開始
    for i in range (2010,2022): 
        for j in range(1,13):
            if j <10:
                j="0"+str(j)
            # 如果日期大於今天日期，停止迴圈(不新增進dates list中)
            if  (str(i)+str(j)+str("01")) > now_time:
                break
            dates.append(str(i)+str(j)+str("01"))

    json_list=[]
    json_data=[]
    #計數
    count = 0
    #把日期反轉，讓程式從最近的日期往前抓，好處是有些股票上市日期不到10年，或是中途下市(只會抓到重新上市後的資料)
    dates.reverse()
    # tqdm 是進度條的插件
    for Date in tqdm(dates):
        try:
            url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={Date}&stockNo={stockNo}'
            #設成空值 (好像沒效果)
            data = None 
            data = requests.get(url).text
            json_data = js.loads(data)
            #用insert是為了讓舊資料在前面
            json_list.insert(0,json_data['data'])
            time.sleep (random.randrange(2, 4))
#             print(Date+" "+f'{stockNo}')
        except:
            # 錯誤計數，如果次數大於3次，就換下一支股票
            count += 1
            if count > 3:
                count = 0
                break
            print("No data of",Date,Name)
            # 把缺失的日期插回list中，這樣就可以繼續抓
            dates.insert(0,Date)
            # 確定缺失的日期在list的第一個
#             print(dates[0])
            continue

    json=[] 
    json_stock=[]
#     try:
    for i in range (0, len(json_list)):
        for j in range(0,len(json_list[i])):
            json_stock.append(json_list[i][j])

    for j in range(0,(len(json_stock))):
        StockPrice = pd.DataFrame(json_stock, columns = ['Date','Volume','Volume_Cash','Open','High','Low','Close','Change','Order'])

        StockPrice['Date'] = StockPrice['Date'].str.replace('/','').astype(int) + 19110000
        StockPrice['Date'] = pd.to_datetime(StockPrice['Date'].astype(str))
        StockPrice['Volume'] = StockPrice['Volume'].str.replace(',','').astype(float)
        StockPrice['Volume_Cash'] = StockPrice['Volume_Cash'].str.replace(',','').astype(float)
        StockPrice['Order'] = StockPrice['Order'].str.replace(',','').astype(float)

#         StockPrice['Open'] = StockPrice['Open'].str.replace(',','').astype(float)
#         StockPrice['High'] = StockPrice['High'].str.replace(',','').astype(float)
#         StockPrice['Low'] = StockPrice['Low'].str.replace(',','').astype(float)
#         StockPrice['Close'] = StockPrice['Close'].str.replace(',','').astype(float)
        StockPrice['Change'] = StockPrice['Change'].str.replace(',','').str.replace('+','').str.replace('X','').astype(float)
        StockPrice.insert(0,column='stock_id',value=stockNo)
        StockPrice.insert(1,column='stock_name',value=Name)
        StockPrice = StockPrice[['stock_id','stock_name','Date','Volume','Volume_Cash','Open','High','Low','Close','Change','Order']]
            #中文對照：股票代碼/公司名稱/日期/成交量/成交金額/開盤價/最高價/最低價/收盤價/漲跌幅/交易筆數
#     except:
#         print("Woops, Something wrong~")

    file_name = "daily/{}_daily.csv".format(stockNo)
    StockPrice.to_csv(file_name, index=False)
    print(file_name+"下載完成...", end="")
    endtime= datetime.now() #紀錄爬取該支股票要多久
    print("執行時間:",endtime-starttime,"秒") #紀錄爬取該支股票要多久
    #1101_daily.csv下載完成...執行時間: 0:12:27.472259 秒
    #1102_daily.csv下載完成...執行時間: 0:12:47.176578 秒

with open('stock_list.csv', encoding='UTF-8') as f:
    list_of_stock = csv.DictReader(f)
    
    #設定之前已經載下來的股票代碼
    stop = 1304
    stop = str(stop)
    num = 2000
    
    #找Index值，從成功的下一隻股票開始找
    for obj in list_of_stock:
        if obj['stock_id'] == stop:
            num = int(obj[''])
            continue
        if int(obj['']) > num :
            print(obj['stock_id']+" "+obj['stock_name'])
            Stock_crawl(obj['stock_id'],obj['stock_name'])
            
#         print(obj['stock_id']+" "+obj['stock_name'])
#     print(list_of_stock)
#     for obj in list_of_stock:
#     Stock_crawl(obj['stock_id'],obj['stock_name'])
#     Stock_crawl(2603,"長榮")