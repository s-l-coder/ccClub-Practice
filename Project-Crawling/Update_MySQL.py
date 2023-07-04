import pymysql
import re


#資料庫連線設定
db = pymysql.connect(host='0.tcp.jp.ngrok.io', port=14080, user='root', passwd='0624', db='fastapi', charset='utf8')
#建立操作游標
cursor = db.cursor()
#SQL語法

#新增資料語法insertinto
sql = "INSERT INTO info(serial_no, name, category, organization_name, url, content, condition_list) VALUES (%s, %s, %s, %s, %s, %s ,%s)"      
#開啟更新檔(記得修改檔案的相對路徑)
f = open('爬蟲練習/crawling_result_test.txt','r', encoding="utf-8")

while True:
    try:
        if f.readline() == "":
            break
        else:
            serial_no_1 = f.readline()
            name_1 = f.readline()
            category_1 = f.readline()
            organization_name_1 = f.readline()
            content_1 = f.readline()
            condition_list_1 = f.readline()
            url_1 = f.readline()
            new_data = (serial_no_1, category_1, organization_name_1, url_1, content_1, condition_list_1, name_1)
            #更新資料語法update 資料表名稱 SET 欄位=數值 WHERE條件式
            #記得修改資料表位置
            update_subsidy = " \
            UPDATE info SET serial_no = %s, category = %s, organization_name = %s, url = %s, content = %s, condition_list = %s  \
            WHERE name = %s"  #變數位置都要跟上面new_data一樣
            cursor.execute(update_subsidy, new_data) #執行指令
            db.commit() #提交至SQL指令
            print('success')

    except EOFError:
        break
        
#發生錯誤時停止執行SQL
    except Exception as e:
        db.rollback()
        if  re.search(r'Duplicate entry', str(e)):
            update_subsidy = "UPDATE info SET serial_no = %s, category = %s, organization_name = %s, url = %s, content = %s, condition_list = %s WHERE name = %s"
            values = (serial_no_1, category_1, organization_name_1, url_1, content_1, condition_list_1, name_1)
            cursor.execute(update_subsidy, values)
            db.commit()
            print('update')
            continue
        else:   
            print('error')
            print(e)
            break

#關閉連線
db.close()
