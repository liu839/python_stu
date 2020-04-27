def cheuk(list_1,number):
    list_temp=[]
    list_2=[]
    list_1.reverse()
    x=0
    for _ in range(len(list_1)+1):
        try:
            list_temp.append(list_1.pop())
        except IndexError:
            list_2.append(list_temp)
            return list_2
        x+=1
        if x==number:
            x=0
            list_2.append(list_temp)
            list_temp=[]
list_1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cheuk(list_1,2))