print('你好')
aa = abs(-20)
print(aa)


age = 61
if age > 18 and age < 60:
    print('')
    print('你成年了。')
elif age > 60:
    print('你退休了。')
else:
    print('你还没有成年啊')

price = 0
for x in [1,2,3,4,5,6,7,8,9]:
    price = price + x
print(price)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(x)


n = 1
while n <= 100:
    if n % 2 == 0:
        print(n)
    n = n + 1

nams = {'张三':90,'李四':50,'王五':85}
print('张三的成绩是' + str(nams['张三']))