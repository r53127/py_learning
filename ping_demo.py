import subprocess

cmd="cmd.exe"
begin=1
end=200
while begin<end:

    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,
                   stdin=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    address="ping 192.168.31."+str(begin)+"\n"
    p.stdin.write(address.encode())
    p.stdin.close()
    p.wait()
    print("execution result: %s"%p.stdout.read().decode("gbk"))
    begin=begin+1
