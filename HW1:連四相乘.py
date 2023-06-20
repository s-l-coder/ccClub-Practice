'''
連四相乘
題目敘述：
給定 k 個（k >= 4）依數大小由小至大排序的整數，找出這些數中挑 4 個數字相乘的最大值。
輸入為一行，包含 k 個整數（k >= 4），數字以空白為間隔。
輸出為一行，包含一個整數。

Sample Output:
-7 -7 1 2 3 4 5 6 7 8 → 2744
1 2 3 4 → 24
'''

num = input().split()
#實際列出各種情況會發現，不論怎樣都只需要比較左四個數＆右四個數＆左二右二數的大小
right_count4 = int(num[-1]) * int(num[-2]) * int(num[-3]) * int(num[-4])
left_count4 = int(num[0]) * int(num[1]) * int(num[2]) * int(num[3])
left2_right2 = int(num[-1]) * int(num[-2]) * int(num[0]) * int(num[1])
count_max = [ right_count4, left_count4, left2_right2 ]
print(max(count_max))
