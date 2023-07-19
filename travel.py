# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:36:14 2023

@author: user
"""

# =============================================================================
# 爬取時尚玩家的旅行頁面資料
# =============================================================================

import requests
from bs4 import BeautifulSoup
import random
import mydb

cursor = mydb.conn.cursor()

url = 'https://supertaste.tvbs.com.tw/travel'

travel = requests.get(url).text #針對網址去串流，將串流資料轉成文字才能用

# print(travel)

# html 解析

sp = BeautifulSoup(travel,'html.parser')

#find只抓取一筆資料
items = sp.find('div',class_='article__content')

#find_all抓取資料時，會用 串列 方式儲放(可存在資料庫)
allTravel = items.find_all('a')

# print(allTravel[0])

for allT in allTravel:
    img = allT.find('img') #抓img的標籤
    img = img.get('data-original') #抓取img內部的屬性
    title = allT.find('h3').text.strip() #抓標題
    pdate = allT.find('span').text.strip() #抓內容文字
    price = random.randint(1000, 9999) #網頁沒價格，用亂數自己給
    
    #連上資料集後，要寫sql語法來將資料寫進資料庫
    sql = "insert into travel(title,photo_url,create_date,price,discount,content) values('{}','{}','{}','{}','{}','{}')".format(title,img,pdate,price,price,title)
    
    cursor.execute(sql) #執行SQL語法
    mydb.conn.commit() #立即提交(馬上更新到資料庫去，而非佔存檔)

mydb.conn.close() #整個資料抓取完畢後，才將此連線關閉

    
