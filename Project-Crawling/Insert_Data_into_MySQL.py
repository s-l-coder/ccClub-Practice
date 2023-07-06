import pymysql


#資料庫連線設定
db = pymysql.connect(host='linebot-subsidy-mysql.fly.dev', port=3306, user='guest', passwd='theflymysql', db='Allowance_Master', charset='utf8')
#建立操作游標
cursor = db.cursor()
#SQL語法

sql = "INSERT INTO AllowanceDetails(serial_no, name, category, organization_name, url, content, condition_list) VALUES (%s, %s, %s, %s, %s, %s, %s);"
f = open('爬蟲練習/subsidy_crawling_result_20230706.txt','r',encoding="utf-8")

while True:
    try:
        serial_no = f.readline()
        name = f.readline()
        category = f.readline()
        organization_name = f.readline()
        title_1 = f.readline() #服務內容
        content = f.readline()
        title_2 = f.readline() #申辦資格
        condition_list = f.readline()
        url = f.readline()
        new_data = (serial_no, name, category, organization_name, url, content, condition_list)
        cursor.execute(sql,new_data)
        db.commit()  #提交修改
        print('success')
    except EOFError:
        break
    except Exception as e:  #發生錯誤時停止執行SQL
        db.rollback()
        print('error')
        print(e)

#關閉連線
db.close()