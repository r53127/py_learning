#coding=utf-8
f=open('hotel_info.json','r')
print(type(f))
print(f.read())

print(f.read())
#f.close()如果不关闭文件，第二次print文件内容为空
f=open('hotel_info.json','r')
print(f.read())