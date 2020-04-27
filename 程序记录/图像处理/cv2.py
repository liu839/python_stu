from cv2 import cv2

img_1=cv2.imread(r"C:\Users\71037\Desktop\zhuangbei.jpg",0)
img_2=cv2.imread(r"C:\Users\71037\Desktop\tujian.jpg",0)

def cv_show(name,img):
	cv2.imshow(name,img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#img_1=cv2.resize(img_1,(0,0),fx=1/3,fy=1/3)    #图片按比列扩大缩小
#res=cv2.addWeighted(img_1,0.4,img_2,0.6,0)      #两图片叠加显示,亮度按比例显示
cv_show('img',img_1)

#b,g,r=cv2.split(img)                           #bgr三通道分离
#cat=img[400:670,380:620]                       #把图片在某个像素段剪切
#cv_show("装备",cat)
#print(img.size)
#cur_img=img.copy()

#cur_img[:,:,1]=0                               
#cur_img[:,:,2]=0
#cv_show('b',cur_img)                           #把图片的1,2通道设置为0,即只显示B通道

