
import socket

print("测试中===========")

s = socket.socket()

host = socket.gethostname()
print(host)
port = 63214
s.connect((host, port))

while True:
    res = s.recv(1024).decode()
    if res == " ":
        break
    print("收到内容%s" % res)

s.close()
