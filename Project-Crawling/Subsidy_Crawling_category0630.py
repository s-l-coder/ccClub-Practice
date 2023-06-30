import requests
from bs4 import BeautifulSoup
import time
import re

url_list = []
subsidy_name_list = []
subsidy_list = []
result = {}
# 加入headers以偽裝我們的真實身分
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }
#設定網址
url_baby = "https://www.gov.tw/News3_Content.aspx?n=2&s=375315"
url_scholarship = "https://www.gov.tw/News3_Content.aspx?n=2&s=381247"
url_laborpassway = "https://www.gov.tw/News3_Content.aspx?n=2&s=389555"
url_passaway = "https://www.gov.tw/News3_Content.aspx?n=2&s=371250"


url_list.append(url_baby)
url_list.append(url_scholarship)
url_list.append(url_laborpassway)
url_list.append(url_passaway)
criteria = {"birth":"","students":"","labor":"","lowincome":"","disabled":"","elder":"","house":"","passaway":""}
def crawling_subsidy(url):
    subsidy_list = []
    
    response = requests.get(url , headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find("div", class_= "simple-text title").getText()
    subsidy_name_list.append(titles)
    #利用findAll爬津貼頁面下方所有內容，然後用for迴圈＆getText取文字值就好
    for contents_test in soup.findAll("div", class_= "css-tr", limit = 2):
        subsidy_list.append(contents_test.getText(strip = True)) #把抓到的前兩項內容先取文字後,放在串列中
        result[titles] = subsidy_list  #把服務跟資格做成字典的value
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
    #name是津貼名稱, 指定進去
    name = titles
    if "兒童" in name or "生育" in name or "育嬰" in name or "育兒" in name or "幼兒" in name or "早期療育" in name:
        criteria['birth'] = name
    if "獎學金" in name or "獎助學金" in name or "就學" in name or "教育" in name or "學費" in name:
        criteria['students'] = name
    if "國民年金" in name or "勞工" in name or "勞保" in name or "就業" in name or "職業災害" in name or "職災" in name or "職保" in name or "就保" in name or "失業" in name or "工作" in name:
        criteria['labor'] = name
    if "弱勢" in name or "中低收入" in name or "中低老人" in name or "經濟弱勢" in name or "低收入戶" in name:
        criteria['lowincome'] = name
    if "身心障礙" in name or "身障" in name or "障礙" in name:
        criteria['disabled'] = name
    if "老人" in name or "老年" in name:
        criteria['elder'] = name
    if "修繕" in name or "租賃" in name or "住屋" in name or "房屋" in name or "租金" in name or "住宅" in name or "租屋" in name  or "購屋" in name:
        criteria['house'] = name
    if "喪葬" in name or "死亡" in name or "身故" in name:
        criteria.append('passaway': 'name')

    
    url = url
    
    #設定是我們要的標題才印出來
    if content_1_title == '服務內容' and content_2_title == '申辦資格':
        print(criteria)
        print(name)
        print(content_1_title,"：")
        print( content_1 ) 
        print(content_2_title,"：")
        print( content_2 )
    else:
        print('津貼內文標題不符')


# for u in url_list跑所有的網址
for u in url_list:
    crawling_subsidy(u)
    #取各分類中的津貼標題
    
print('生育及育兒相關津貼:',criteria['birth'])
print('學生相關津貼:',criteria['students'])
print('國民年金及勞工相關津貼:',criteria['labor'])
print('中低收入相關津貼:',criteria['lowincome'])
print('身心障礙相關津貼:',criteria['disabled'])
print('長者礙相關津貼:',criteria['elder'])
print('房屋相關津貼:',criteria['house'])
print('親屬身故給付相關津貼:',criteria['passaway'])

    
    
    