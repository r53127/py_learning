import win32api
import win32print

filename=open("./1.txt",'w')
filename.write('test')
filename.close()
win32api.ShellExecute(0,"print",filename,'/d:"%s"'%win32print.GetDefaultPrinter(),".",0)


