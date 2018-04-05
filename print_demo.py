import linecache
import random
import re
import time
import win32api
import win32print

#linecache只能读取UTF-8文件


hotelname=input("请输入餐馆名：")
print_date=input('请输入打印时间：')
people=input('请输入人数：')
sum_input=input('请输入用餐金额：')
account=int(sum_input)
filename='1.txt'
if account<=500:
    open(filename,'w+').write("餐别：午餐  餐馆名称："+hotelname+'  人数：'+people+'\n')
else:
    open(filename, 'w+').write("餐别：晚餐  餐馆名称：" + hotelname + '  人数：' + people + '\n')
open(filename,"a+").write('打印时间：'+print_date+' '+time.strftime("%H:%M:%S", time.localtime())+'\n')
open(filename,'a+').write('''--------------------------------------------
消费清单           数量     单价      金额  
--------------------------------------------\n
''')
item_list=[]
dish_sum=0
if account>500:
    while dish_sum<1000:#for循环几次
        a = random.randrange(1,246)#1-9中生成随机数
        #从文件中对读取第a行的数据
        theline = linecache.getline('dish_menu.txt', a)
        #匹配中文菜名
        dish_item=re.search("[\u4e00-\u9fa5]+",theline)
        #如果匹配成功则写入
        if dish_item!=None:
            item=dish_item.group()
            if item not in item_list:
                item_price=random.randrange(100,200)
                dish_sum = dish_sum + item_price
                if dish_sum<=1000:
                    open(filename,'a+').write(item.ljust(10)+'\000'*(10-len(item))+'1       '+'%s.00' %str(item_price)+'   '+'%s.00' %str(item_price)+'\n')
                else:
                    open(filename, 'a+').write(
                    item.ljust(10) + '\000' * (10 - len(item)) + '1       ' + '%s.00' %str(1000-dish_sum+item_price) + '   ' + '%s.00' %str(
                        1000-dish_sum+item_price) + '\n')
                item_list.append(item)

            else:
                continue
        else:
            continue
else:
    while dish_sum<account:#for循环几次
        a = random.randrange(1,246)#1-9中生成随机数
        #从文件中对读取第a行的数据
        theline = linecache.getline('dish_menu.txt', a)
        #匹配中文菜名
        dish_item=re.search("[\u4e00-\u9fa5]+",theline)
        #如果匹配成功则写入
        if dish_item!=None:
            item=dish_item.group()
            if item not in item_list:
                item_price=random.randrange(100,200)
                dish_sum = dish_sum + item_price
                if dish_sum<=account:
                    open(filename,'a+').write(item.ljust(10)+'\000'*(10-len(item))+'1       '+'%s.00' %str(item_price)+'   '+'%s.00' %str(item_price)+'\n')
                else:
                    open(filename, 'a+').write(
                        item.ljust(10) + '\000' * (10 - len(item)) + '1       ' + '%s.00' %str(account-dish_sum+item_price) + '   ' + '%s.00' %str(
                        account-dish_sum+item_price) + '\n')
                item_list.append(item)
            else:
                continue
        else:
            continue
if account>500:
    open(filename, 'a+').write('''
--------------------------------------------
优惠金额：0.00元
应付金额：1000.00元
--------------------------------------------
''')
else:
    open(filename, 'a+').write('''
--------------------------------------------
优惠金额：0.00元
应付金额：''')
    open(filename,'a+').write(str(account)+'''元
--------------------------------------------
    ''')
#print(dish_sum)
win32api.ShellExecute(0,"print",filename,'/d:"%s"' %win32print.GetDefaultPrinter(),".",0)