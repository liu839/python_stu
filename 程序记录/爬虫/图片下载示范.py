import urllib.request

req=urllib.request.Request("https://i2.hdslb.com/bfs/archive/fed85268cdb95352121d7ebea9f5d92880c9875a.jpg@217w_133h.webp")
response=urllib.request.urlopen(req)
img=response.read()
with open(r"C:\Users\71037\Desktop\666.jpg",'wb') as f:
    f.write(img)
#图片链接会变