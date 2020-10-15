def solve(num_list):
    lens = len(num_list)
    for i in range(1,lens):
        for j in range(1,len(num_list[i])-1):
            num_list[i][j] = max(num_list[i-1][j],num_list[i-1][j-1]) + num_list[i][j]
    print("结果为"+str(max(num_list[-1]))+"\n")

def get():
    num_list = []
    while True:
        temp = input("请以,分割数值输入三角形每一行.输入回车表示结束\n>")
        if temp == "":
            break
        try:
            num_list.append([int(each) for each in temp.split(",")])
        except:
            print("数据输入错误,请重新输入\n")
    lens = len(num_list)
    if lens == 0:
        print("未检测到任何输入\n")
        return 0
    if lens == 1:
        print("结果为"+str(num_list[0][0])+"\n")
    for i in range(lens):
        num_list[i].append(0)
        num_list[i].insert(0,0)
    solve(num_list)

while True:
    get()
    if input("输出!以结束程序: ") == "!":
        break