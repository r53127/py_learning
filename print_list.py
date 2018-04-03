import tempfile
import win32api
import win32print

filename=tempfile.mktemp("a.txt")
open(filename,"w").write("This is a test file")
win32api.ShellExecute(0,"print",filename,'/d:"%s"' %win32print.GetDefaultPrinter(),".",0)