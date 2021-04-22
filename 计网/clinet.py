'''创建客户端'''
import socket
import base64

def reve():
    print("收到的服务的消息：")
    res = s.recv(1024).decode()
    print(res)
    decode = base64.b64decode(res)
    decode = ''.join(chr(each) for each in decode.split(" "))
    print(decode.decode("utf8"))

def send():
    sends = input("客户端发送的消息：")
    if sends == 'qq':
        raise SystemError
    sends = s.send(base64.b64encode(sends.encode()))

print("连接中===========")

host = '192.168.43.21'
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