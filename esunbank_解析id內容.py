# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 12:48:29 2023

@author: User
"""
#作業1:以 玉山銀行牌告匯率 解析id內容

import requests
from bs4 import BeautifulSoup

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

data = requests.get(url,headers=header).text

soup = BeautifulSoup(data,'html.parser')

rates = soup.find(id='exchangeRate') # 利率 找id [匯入id]

tbody = rates.find('tbody')

trs = tbody.find_all('tr')[2:] # 從第2行開始


for row in trs:
    tds = row.find_all('td',recursive = False) # recursive遞迴
    print(row)
    break
    #if len(tds) == 4:
    #    print(tds[0].text.strip())
    #    print(tds[1].text.strip())
    #    print(tds[2].text.strip())
    #    print(tds[3].text.strip())
    #    print()
    