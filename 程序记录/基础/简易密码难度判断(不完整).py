temp=input('请输入需要检测的密码组合')
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
judge_1=0
judge_2=0
sum=len(temp)

for i in temp:
    if i in symbols and i in chars and i in nums:
        judge_2+=1
    if temp.istitle():
        judge_2+=1
if sum<=8:
    if temp.isdecimal() or temp.isalpha():
        print('低级密码')
if sum>8 and sum<=16:
    for i in temp:
        if i in symbols:
         judge_1+=1
        if i in chars:
         judge_1+=1
        if i in nums:
         judge_1+=1
    if judge_1==2:
        print('中级密码')
if sum>16:
    for i in temp:
     if i in symbols and i in chars and i in nums:
          judge_2+=1
     if temp.istitle():
          judge_2+=1
     if judge_2==2:
        print('高级密码')
