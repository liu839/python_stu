import openpyxl
import os

list_1 = [ [], [], [], [], []]
list_2 = [ [], [], [], [], []]
list_3 = [ [], [], [], [], []]

filename1=r'C:\Users\71037\Desktop\周考14.xlsx'
dirname=r'C:\Users\71037\Desktop\新建文件夹 (2)'
os.chdir(dirname)

wb1=openpyxl.load_workbook(filename1)
ws1=wb1["Sheet1"]


temp_a = 'C' #标号为C
temp_left = temp_a+"2"
number=11
for index in range(len(list_1)):
    temp_right = temp_a+str(number)
    for each in ws1[temp_left:temp_right]:
        for i in each:
            list_1[index].append(i.value)
    number+=10

temp_a = 'C' #标号为C
temp_left = temp_a+"185"
number=194
for index in range(len(list_2)):
    temp_right = temp_a+str(number)
    for each in ws1[temp_left:temp_right]:
        for i in each:
            list_2[index].append(i.value)
    number+=10

temp_a = 'C' #标号为C
temp_left = temp_a+"302"
number=311
for index in range(len(list_3)):
    temp_right = temp_a+str(number)
    for each in ws1[temp_left:temp_right]:
        for i in each:
            list_3[index].append(i.value)
    number+=10

list_dirname=os.listdir(dirname)
for eachname in list_dirname:
    wb2=openpyxl.load_workbook(eachname)
    ws2=wb2["Sheet1"]

    temp_left = temp_a+"2"
    number=11
    for index in range(len(list_1)):
        temp_right = temp_a+str(number)

        temp=[]
        for each in ws2[temp_left:temp_right]:
            for i in each:
                temp.append(i.value)

        list_1[index]=[x for x in list_1[index] if x in temp]
        number+=10

    temp_left = temp_a+"185"
    number=194
    for index in range(len(list_2)):
        temp_right = temp_a+str(number)
        temp=[]
        for each in ws2[temp_left:temp_right]:
            for i in each:
                temp.append(i.value)
        list_2[index]=[x for x in list_2[index] if x in temp]
        number+=10

    temp_left = temp_a+"302"
    number=311
    for index in range(len(list_3)):
        temp_right = temp_a+str(number)
        temp=[]
        for each in ws2[temp_left:temp_right]:
            for i in each:
                temp.append(i.value)
        list_3[index]=[x for x in list_3[index] if x in temp]
        number+=10

for index in reversed(range(len(list_1))):
    if index == 0:
        break
    list_1[index]=[x for x in list_1[index] if x not in list_1[index-1]]

for index in reversed(range(len(list_2))):
    if index == 0:
        break
    list_2[index]=[x for x in list_2[index] if x not in list_2[index-1]]

for index in reversed(range(len(list_3))):
    if index == 0:
        break
    list_3[index]=[x for x in list_3[index] if x not in list_3[index-1]]

for each in list_1:
    print(each)
for each in list_2:
    print(each)
