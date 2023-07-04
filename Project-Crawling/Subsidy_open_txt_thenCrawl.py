# 目標:寫出利用讀文字檔案套用爬蟲function的結果
# 待處理: KeyError部分 line 51
import requests
from bs4 import BeautifulSoup
import random
import time
import re
#創立津貼所有網址的list 等下可以接
url_list = []
subsidy_name_list = []
#打開Claire爬好的網址檔案
f = open('爬蟲練習/name_oragn_url.txt','r',encoding="utf-8")

for line in f.readlines():
    subsidy = line.split("$$$")
    name = subsidy[0] #津貼名稱
    organ = subsidy[1] #中央或地方政府
    url = subsidy[2] #網址
    url_list.append(url)
    subsidy_name_list.append(name)

f.close
print(subsidy_name_list)
print(url_list)


subsidy_list = []
result = {}
# 加入headers以偽裝我們的真實身分
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }

content_1_p = ""
content_1_title = ""
content_1 = ""
content_2_p = ""
content_2_title = ""
content_2 = ""

def crawling_subsidy(url, name):
    subsidy_list = []
    category_list = []
    response = requests.get(url , headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    # titles = soup.find("div", class_= "simple-text title").getText()
    
    #利用findAll爬津貼頁面下方所有內容，然後用for迴圈＆getText取文字值就好
    for contents_test in soup.findAll("div", class_= "css-tr", limit = 2):
        subsidy_list.append(contents_test.getText(strip = True)) #把抓到的前兩項內容先取文字後,放在串列中
        result[name] = subsidy_list  #把服務跟資格做成字典的value
    
    # for name in subsidy_name_list:
    #服務內容這邊的資料等於content_1_p
    content_1_p = result[name][0]
    #把標題跟內文用slice方式分開取用
    content_1_title = result[name][0][0:4]
    content_1 = result[name][0][4:]
    #申辦資格資料等於content_2_p
    content_2_p = result[name][1]
    #把標題跟內文用slice方式分開取用
    content_2_title = result[name][1][0:4]
    content_2 = result[name][1][4:]

    if re.findall(r'育兒|兒童|生育|育嬰|幼兒|早期療育', name):
        category_list.append('birth')
    if re.findall(r'獎學金|獎助學金|就學|教育|學費', name):
        category_list.append('students')
    if re.findall(r'國民年金|勞工|勞保|就業|職業災害|職災|職保|就保|失業|工作', name):
        category_list.append('labor')
    if re.findall(r'弱勢|中低收入|中低老人|經濟弱勢|低收入戶', name):
        category_list.append('lowincome')
    if re.findall(r'身心障礙|身障', name):
        category_list.append('disabled')
    if re.findall(r'老人|老年', name):
        category_list.append('elder')
    if re.findall(r'修繕|租賃|住屋|房屋|租金|住宅|租屋|購屋', name):
        category_list.append('house')
    if re.findall(r'喪葬|死亡|身故', name):
        category_list.append('passaway')
    #category是津貼種類, 指定進去,用join從category_list串列取出成字串
    category = ', '.join(category_list)
    #url是津貼網址, 指定進去
    url = url
    #津貼編號
    serial_no = int(url[-6:])
    #政府單位
    organization_name = organ #在上一個打開檔案的區塊有定義
        
    if content_1_title == '服務內容' and content_2_title == '申辦資格':
        print(serial_no)
        print(name)
        print(category)
        print(organization_name)
        print(content_1_title,"：")
        print(content_1) 
        print(content_2_title,"：")
        print(content_2)
        print(url)
    elif content_1_title == '服務內容':
        print(serial_no)
        print(name)
        print(category)
        print(organization_name)
        print(content_1_title,"：")
        print(content_1) 
        print('申辦資格 ：') 
        print('無')
        print(url)
    else:
        print('津貼內文標題不符')
        print(serial_no)
        print(name)
        print(category)
        print(organization_name)
        print(content_1_title,"：")
        print(content_1) 
        print(content_2_title,"：")
        print(content_2)
        print(url)
    

# for u in url_list跑所有的網址
for u in url_list:
    for name in subsidy_name_list:
        #寫入結果檔案
        with open("Subsidy_Crawling_Result.txt", mode='w', encoding="utf-8") as file:
            file.write(crawling_subsidy(u, name))
