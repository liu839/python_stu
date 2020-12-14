'''创建客户端'''
import socket
import base64

def reve():
    print("\n收到的服务的消息：")
    res = s.recv(1024)
    print("收到的原数据",res)
    decode = base64.b64decode(res).decode("utf-8")
    decode = ''.join(chr(int(each)) for each in decode.strip().split(" "))
    print("解析结果为：",decode)

def send():
    sends = input("客户端发送的消息：")
    if sends == 'qq':
        raise SystemError
    sends = ' '.join([str(ord(each))for each in sends])
    sends = s.send(base64.b64encode(sends.encode('utf-8')))

print("连接中===========")

host = '192.168.3.29'
port = 63214
s = socket.socket()
s.connect_ex((host, port))
print("已建立链接！")
try:
    while True:
        reve()
        send()
except SystemError:
    s.close()