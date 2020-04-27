from PIL import Image
img=Image.open(r"C:\Users\71037\Desktop\666.jpg")
out=img.convert("L")
out=out.resize((700,400))
asciis="A897531"
text=""
f=open(r'C:\Users\71037\Desktop\新建文本文档.txt','w')
for row in range(400):
    for col in range(700):
        grey=out.getpixel((col,row))
        text=asciis[int(grey/255*6)]
        f.write(text)
    f.write('\n')
f.close()