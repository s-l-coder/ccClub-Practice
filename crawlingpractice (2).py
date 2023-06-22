#先import模組
import requests
from bs4 import BeautifulSoup
import time
#建立所需項目的空串列
url_list = []
subsidy_name_list = []
subsidy_list = []

# 加入headers以偽裝我們的真實身分
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }
#設定網址
url_baby = " https://www.gov.tw/News3_Content.aspx?n=2&s=375315"
response = requests.get(url_baby , headers = headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
#CSS定位練習
for content in soup.select('div[class="group-tab default"] div[class="indent"] ul'):
    subsidy_list.append(content.text.replace('\n', ' ').replace('\xa0', ' '))
print(subsidy_list[0])
print(subsidy_list[1])

#利用findAll爬津貼頁面下方所有內容，然後用for迴圈＆getText取文字值就好
# for contents_test in soup.findAll("div", class_= "css-tr", limit = 2):
#     #print(contents_test.getText())
#     subsidy_list.append(contents_test.getText(strip = True))


#取得津貼標題文字
titles = soup.find("div", class_= "simple-text title").getText()
subsidy_name_list.append(titles)
# #依序印出津貼名字、服務內容、申辦資格
# print(titles)
# print(subsidy_list[0])
# print(subsidy_list[1]) 
# print(type(subsidy_list[0]))

#原本想要'服務內容'跟'申辦資格'分開抓,但用find會失敗,因為只能抓到同標籤第一個項目
#所以criteria這項是錯的
criteria = soup.find("div", class_= {"css-td","li"}).getText()
# print(allcontent)
# print(criteria)