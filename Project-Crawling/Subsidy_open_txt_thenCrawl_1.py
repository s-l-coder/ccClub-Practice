# 目標:寫出利用讀文字檔案套用爬蟲function的結果
# 待處理: KeyError部分
import requests
from bs4 import BeautifulSoup
import random
import datetime
import time
import re

delay_choices = [1, 3, 2, 11, 5, 7]  #延遲的秒數
delay = random.choice(delay_choices)  #隨機選取秒數
time.sleep(delay)  #延遲

#創立津貼所有網址的list 等下可以接
url_list = []
subsidy_name_list = []
organization_list = []
#打開Claire爬好的網址檔案
f = open('name_organ_url.txt','r',encoding="utf-8")

for line in f.readlines():
    subsidy = line.split("$$$")
    name = subsidy[0] #津貼名稱
    organ = subsidy[1] #中央或地方政府
    url = subsidy[2].rstrip('\n') #讀取檔案會遇到換行\n符號出現的問題, 用 .rstrip('\n') 解決
    url_list.append(url)
    organization_list.append(organ)
    subsidy_name_list.append(name)

f.close
# print(subsidy_name_list)
# print(url_list)
subsidy_name_url_dict = {}
subsidy_name_url_dict= dict(zip(subsidy_name_list, url_list))
name_organ_dict = dict(zip(subsidy_name_list,organization_list))
# print(subsidy_name_url_dict)

subsidy_list = []
result = {}
# 加入headers以偽裝我們的真實身分
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }

def crawling_subsidy(url):
    subsidy_list = []
    category_list = []
    response = requests.get(url , headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find("div", class_= "simple-text title").getText()
    
    #利用findAll爬津貼頁面下方所有內容，然後用for迴圈＆getText取文字值就好
    for contents_test in soup.findAll("div", class_= "css-tr", limit = 2):
        subsidy_list.append(contents_test.getText(strip = True)) #把抓到的前兩項內容先取文字後,放在串列中
        result[titles] = subsidy_list  #把服務跟資格做成字典的value
    
    # for name in subsidy_name_list:
    #服務內容這邊的資料等於content_1_p
    content_1_p = result[titles][0]
    #把標題跟內文用slice方式分開取用
    content_1_title = result[titles][0][0:4]
    content_1 = result[titles][0][4:]
    #申辦資格資料等於content_2_p
    content_2_p = result[titles][1]
    #把標題跟內文用slice方式分開取用
    content_2_title = result[titles][1][0:4]
    content_2 = result[titles][1][4:]

    if re.findall(r'育兒|兒童|生育|育嬰|幼兒|早期療育', titles):
        category_list.append('birth')
    if re.findall(r'獎學金|獎助學金|就學|教育|學費', titles):
        category_list.append('students')
    if re.findall(r'國民年金|勞工|勞保|就業|職業災害|職災|職保|就保|失業|工作', titles):
        category_list.append('labor')
    if re.findall(r'弱勢|中低收入|中低老人|經濟弱勢|低收入戶', titles):
        category_list.append('lowincome')
    if re.findall(r'身心障礙|身障', titles):
        category_list.append('disabled')
    if re.findall(r'老人|老年', titles):
        category_list.append('elder')
    if re.findall(r'修繕|租賃|住屋|房屋|租金|住宅|租屋|購屋', titles):
        category_list.append('house')
    if re.findall(r'喪葬|死亡|身故', titles):
        category_list.append('passaway')
    #category是津貼種類, 指定進去,用join從category_list串列取出成字串
    category = ', '.join(category_list)
    #url是津貼網址, 指定進去
    url = url
    #津貼編號
    serial_no = int(url[-6:])
    #政府單位
    organization_name = name_organ_dict[titles] #在上一個打開檔案的區塊有定義
    if titles:
        if content_1_title == '服務內容' and content_2_title == '申辦資格':
            print(serial_no)
            print(titles)
            print(category)
            print(organization_name)
            print(content_1_title,"：")
            print(content_1) 
            print(content_2_title,"：")
            print(content_2)
            print(url)
        elif content_1_title == '服務內容':
            print(serial_no)
            print(titles)
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
            print(titles)
            print(category)
            print(organization_name)
            print(content_1_title,"：")
            print(content_1) 
            print(content_2_title,"：")
            print(content_2)
            print(url)
    else:
        print('此區錯誤:',titles)

for u in url_list:
    crawling_subsidy(u)

# #設定爬蟲日期
# today = datetime.date.today()
# crawling_content_date = today.strftime('%Y%m%d')
# #利用津貼名稱跟網址的字典叫出爬蟲函式所需的變數(網址&津貼名稱)
# #用名稱跑迴圈

# for u in url_list:
#     #寫入結果檔案 利用with open() as不用關閉檔案
#     #設定津貼爬蟲內容清單為subsidy_crawling_result_今天日期.txt
#     crawling_data = str(crawling_subsidy(u))
#     with open(f'subsidy_crawling_result_{crawling_content_date}.txt', mode='w', encoding="utf-8") as file:
#         file.write(crawling_data)

# crawling_subsidy('https://www.gov.tw/News3_Content.aspx?n=2&s=517156')