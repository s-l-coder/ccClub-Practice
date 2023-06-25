import requests
from bs4 import BeautifulSoup
import time

url_list = []
subsidy_name_list = []
subsidy_list = []
result = {}
# 加入headers以偽裝我們的真實身分
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }
#設定網址
url_baby = "https://www.gov.tw/News3_Content.aspx?n=2&s=375315"
url_adopt = "https://www.gov.tw/News3_Content.aspx?n=2&s=371550&lep=8"


url_list.append(url_baby)
url_list.append(url_adopt)


def crawling_subsidy(url):
    subsidy_list = []
    response = requests.get(url , headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find("div", class_= "simple-text title").getText()
    print(titles)
    subsidy_name_list.append(titles)
    #利用findAll爬津貼頁面下方所有內容，然後用for迴圈＆getText取文字值就好
    for contents_test in soup.findAll("div", class_= "css-tr", limit = 2):
        # print(contents_test)
        subsidy_list.append(contents_test.getText().replace('\n'," ")) #把抓到的前兩項內容先取文字後,放在串列中
        result[titles] = subsidy_list  #把服務跟資格做成字典的value
    #服務內容這邊的資料等於content_1_p
    content_1_p = result[titles][0].split(" ")
    #申辦資格資料等於content_2_p
    content_2_p = result[titles][1].split(" ")
    #name是津貼名稱, 指定進去
    name = titles
    url = url
    #利用變數指定方式區分'服務內容'跟'申辦資格'這兩個標題跟裡面的內容
    none, content_1_title, *content_1= content_1_p
    #content_1_title = 服務內容
    none, content_2_title, *content_2= content_2_p
    if content_1_title == '服務內容' and content_2_title == '申辦資格':
        print(content_1_title)
        print( *content_1 )  #用*號解包
        print( *content_2 )
    # return name, url, content_1, return content_2
    
    # print(result[titles][0])
    # print(result[titles][1])

# for u in url_list跑所有的網址
for u in url_list:
    print(crawling_subsidy(u))
    
    
