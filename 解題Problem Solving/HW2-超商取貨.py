'''
HW2:超商取貨
Description
在網拍大行其道的現在，去超商取貨已經成為現代人幸福的來源之一：在網路上下訂單之後，心心念念某天回家經過超商可以順便拿變成喜歡的樣子的工資。超商取貨多半靠手機後三碼找出按後三碼分門別類堆起來的商品後，再搭配身分證件確認取貨人身分。現在，給定商品進貨時的資訊與取貨人報的後三碼，你可以正確地指出誰買了什麼嗎？
保證不會出現姓名及電話後三碼都相同的情形，但有可能出現撞名（但後三碼不一樣），或電話後三碼一樣（但名字不同）的情況。
Input
輸入包含 n + m + 1 行。
前 n 行是進貨資訊，每行包含 10 碼的電話號碼、取貨人姓名、物品，以逗號分隔。
接下來為 end 代表已經讀完進貨資訊了。
最後 m 行是取貨人資訊，每行包含取貨人電話後 3 碼、取貨人姓名，以空格分隔。
Output
輸出有 m 行，為對應的取貨物品。
若查不到取貨人資訊，該行請輸出 Check again!

0912345678,Kevin,Artis
0988123456,KT,white coat
0999123456,yeutong,sour map
0997846678,yuhsuan,ching goat
end
678 yuhsuan
678 Xiao ming →
ching goat
Check again!

0969322347,Krishna,Bird
0973644044,Krishna,Beaver
0993524003,Towney,Duck
end
347 Krishna
044 Tommy Lee → 
Bird
Check again!
'''

import_data = [] #建立進貨資訊串列
collect = [] #建立取貨人資料串列
while True:
    try:
        data= input().split(',')
        if data == ['end'] or []:  #假如輸入end或enter就跳出迴圈不寫入資料
            break
        else:
            import_data.append(data)
    except:
        break
while True:
    try:
        collect_data = input().split(' ',1) #注意名字可能有空格,所以限定分隔數為1
        if collect_data == ['']: #假如未輸入資料就跳出迴圈不寫入取貨人(注意條件判斷的串列形式,空串列長怎樣)
            break
        else:
            collect.append(collect_data)
    except:
        break
#建立電話號碼/姓名/包裹物品的串列,以利等下建立字典用
#因為只取後三碼跟姓名去當字典的key都可能重複,所以併在一起
import_package = []
import_num_name = []
for i in range(0,len(import_data)):
    import_package.append(import_data[i][2])
    import_num_name.append(import_data[i][0][-3::1] + import_data[i][1])
#把後三碼姓名&包裹合成一個字典
dict = dict(zip(import_num_name,import_package))
#用迴圈拿出取貨人後三碼加上電話,去當作key取出上面字典的value(包裹資訊)
for i in range(0,len(collect)):
    print(dict.get(collect[i][0]+collect[i][1],"Check again!"))


