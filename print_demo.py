import win32api
import win32print
import time
import linecache
import random

hotelname=input("请输入餐馆名：")
print_date=input('请输入打印时间：')
filename='1.txt'
open(filename,'w+').write("餐别：晚餐  餐馆名称："+hotelname+'\n')
open(filename,"a+").write('打印时间：'+print_date+' '+time.strftime("%H:%M:%S", time.localtime())+'\n')
open(filename,'a+').write('''-----------------------------------
消费清单   数量     单价      金额  
-----------------------------------\n
''')
for i in range(1,9):#for循环几次
    a = random.randrange(1,20)#1-9中生成随机数
    print(a)
    #从文件中对读取第a行的数据
    theline = linecache.getline('dish_menu.txt', a)
    print(theline)
    #open(filename,'a+').write(theline+'\n')