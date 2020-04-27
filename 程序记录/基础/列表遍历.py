#方法1
count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2

#方法二：    
    
for each in range(len(member)):
    if each%2 == 0:
        print(member[each], member[each+1])