judge = input()
shoppinglist_dict = {}
shoppinglist = []
name_list = []

while True:
    try:
        shoppingdata = input().split(' ')
        name = shoppingdata[0]
        shoppingitem = shoppingdata[1:]
        if shoppingdata == ["end"]:
            break
        else:
            shoppinglist_dict[name] = shoppingitem
            shoppinglist.append(shoppingdata)
            name_list.append(name)
    except EOFError:
        break
# print(shoppinglist_dict)
# print(name_list)
#寫一個計算相似度的方法
#先想辦法知道每個人之間的相似度->知道重複的購買清單
def similaritycheck(A, B):
    def repeatcheck(A, B): #小的function是取兩個串列的交集(也就是重複之處)
        return set(shoppinglist_dict[A]) & set(shoppinglist_dict[B]) 
    similarity = len(list(repeatcheck(A, B))) / len(shoppinglist_dict[A]) #取AB之間與A的相似之處
    return similarity

suggest_list = []
suggest_set= set()
suggest_dict = {}
def suggest(A,B):
    suggest_list = [] #每次讓建議購買清單的先清空
    if similaritycheck(A , B) >= int(judge) / 100: 
        #因為我們前面自訂義函式用除法,所以這裡再用/100
        suggest_item = set(shoppinglist_dict[B]) - set(shoppinglist_dict[A])
        if A not in suggest_dict.keys(): #設定如建議購買字典中沒有人名就新增字典key 
            suggest_dict[A] = list(suggest_item)
        else: 
            #如果已經有key就用extend()新增value(因為可能有多個建議購買)
            #用extend不用append是因為extend會取出元素直接新增(不會變成一個串列物件)
            suggest_dict[A].extend( list(suggest_item) )
        # print(suggest_dict)
    elif similaritycheck(A , B) < int(judge) / 100:
        pass
    else:
        pass

    if A not in suggest_dict.keys(): #設定如建議購買字典中沒有人名就新增字典key 
        suggest_dict[A] = []

    return suggest_dict

# print(suggest(name_list[0],name_list[1]))

for i , name1 in enumerate(name_list): #利用enumerate函式叫出人名
    for index, name2 in enumerate(name_list):
        if name1 == name2:  #讓判斷相似值遇到同樣人名的時候跳過
            pass
        else:
            suggest_list_fin = suggest(name1, name2)
            # print(suggest_list_fin)

for key, value in suggest_list_fin.items():
    new_value = set(value) #去除重複的購買清單
    print(key, *list(new_value))





'''
商務上，常常會依據顧客的消費行為，推薦該顧客消費行為跟他類似的客戶購買的產品。
現在，給定我們有判斷相不相似的閾值以及顧客的購買紀錄，你可以推薦他們購買沒買過的產品嗎？

說明：
以範例一為例子。對凱文來說，小明跟他的相似度是 3/4 = 75% >= 50%，小美是 0/4 = 0% < 50%，小華是 2/4 = 50% >= 50%。
因此，我們推薦凱文小明買過但他沒買過的卡片跟機車，還有小華買過但凱文沒買過的番茄。
在輸出的第一行，我們先輸出凱文，接著依照商品出現的順序依序輸出要推薦給凱文的卡片、機車、番茄。
對小明來說，只有凱文跟他的相似度 3/5 = 60% >= 50%，因此我們推薦他凱文買過但他沒買過的鑰匙。
阿小美就是個邊緣人，我們先不理他。
小華跟小明和凱文的相似度是 2/3 = 67% >= 50%，因此我們推薦他凱文跟小明有買但他沒買的錢包、鑰匙、卡片、機車。
Input
輸入為 n + 2 行。
第一行包含一個整數，為判斷相不相似的閾值。
中間 n 行中，每一行包含數個詞，以空白區隔。
最後一行輸入 end，代表輸入結束。
Output
輸出為 n 行，代表對 n 個顧客的推薦商品。

50
凱文 電腦 手機 錢包 鑰匙
小明 電腦 手機 錢包 卡片 機車
小美 香蕉 蘿蔔
小華 電腦 手機 番茄
end
->
凱文 卡片 機車 番茄
小明 鑰匙
小美
小華 錢包 鑰匙 卡片 機車

50
r S F C D U Q Z
l Q D F S B Z
q Q F U C D
c Z D F U B S Q C
end
->
r B
l C U
q S Z B
c
'''