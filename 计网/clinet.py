<<<<<<< HEAD
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
=======
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
>>>>>>> aa400b7fa14aa9355fbc79b36f7c826e607904da
    s.close()