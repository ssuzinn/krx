import time
import os
import tqdm
import glob
from datetime import date,datetime
from pykrx import stock
import pandas as pd

dateRange=pd.date_range(start="2019-01-01",end="2022-02-01")

def ticker(dd):
    stock_code= stock.get_market_ticker_list(date=dd,market="ALL")
    L=len(stock_code)
    stock_code.append(L)
    with open(f'krx/data/ohlc/{dd}_stock_code.txt','w') as f:
        for line in stock_code:
            f.write(str(line)+'\n')
    f.close()

def ohlc(dd):
    if os.path.isfile(f'krx/data/ohlc/{dd}_stock_ohlc.csv') is False:
        df = stock.get_market_price_change_by_ticker(fromdate=dd, todate=dd)
        df.to_csv(f'krx/data/ohlc/{dd}_stock_ohlc.csv')

def MCap(dd):
    df = stock.get_market_cap(dd)
    df.to_csv(f'krx/data/mcap/{dd}_stock_mcap.csv')


def merge(folder):
    Dir= f"/Users/sujin/Desktop/sujin/code/krx/data/{folder}/"
    file_type=r"*.csv"
    fileList = glob.glob(Dir+file_type)
    fl=sorted([i.split('/')[-1] for i in fileList])
    
    res = pd.DataFrame()
    for file  in fl:
        df=pd.read_csv(f'krx/data/{file}')
        if df.empty:
            print('!')
            pass
        else:
            date=file.split('_')[0][:4]+'-'+file.split('_')[0][4:6]+'-'+file.split('_')[0][6:]
            df['date']=datetime.strptime(date,'%Y-%m-%d')
            res = pd.concat([res, df], axis=0)
    res = res.reset_index()
    res.to_csv('krx/201901_202201_{folder}.csv')

for d in dateRange:
    dd=d.strftime('%Y%m%d')
    time.sleep(3)
    MCap(dd)
