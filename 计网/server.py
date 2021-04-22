import socket
import base64
s = socket.socket()

inputstr = []

host = socket.gethostname()
#print(host)
port =  63214

add = (host, port)

s.bind(add)

s.listen(5)
print("working ------------")
c, addr = s.accept()
print("accepted ------------\n连接地址：", addr)

def secret_in(inputstr):
    res = ' '.join([str(ord(each)) for each in inputstr])
    res = base64.b64encode(res.encode("utf-8"))
    print("发送的源数据为:",res)
    return res

def secret_out(inputstr):
    print("未解析字符串"+ str(inputstr))
    res = base64.b64decode(inputstr).decode('utf-8')
    res = ''.join([chr(int(each)) for each in res.strip().split(' ')])
    return res

while True:
    inputstr = input("请输入发送内容：")
    res = secret_in(inputstr)
    c.send(res)
    print("accepted------------")

    res =secret_out(c.recv(1024))

    if res.strip():
        print("解析完成后:%s\n" % res)

c.close()