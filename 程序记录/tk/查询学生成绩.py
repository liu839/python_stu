from tkinter import *
master = Tk()
#初始化数据
master.title("查询学生成绩")
number = StringVar()
number_show= StringVar()
name = StringVar()
score_1 = StringVar()
score_2 = StringVar()
score = StringVar()

student_hash = {}
class Student():
    def __init__(self,number,name,score_1,score_2):
        self.number = number
        self.name = name
        self.score_1 = score_1
        self.score_2 = score_2
        self.score = score_1*0.4 + score_2*0.6
students = []
with open(r'C:\Users\71037\Desktop\计算机\python\程序记录\tk\student.txt', 'r') as f:
    data = list(f)
    for index,each in enumerate(data):
        each = each.replace('\n', '')
        each = each.split(' ')
        students.append(Student(each[0],each[1],int(each[2]),int(each[3])))
        student_hash[each[0]] = index


menubar = Menu(master)
choosemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='选择功能', menu=choosemenu)
choosemenu.add_command(label='查找')
choosemenu.add_command(label='添加')
choosemenu.add_command(label='修改')

master.config(menu=menubar)

Label(master, text="输入学号").grid(row=0)

Label(master, text="学号").grid(row=1,column=0)
Label(master, text="姓名").grid(row=1,column=2)
Label(master, text="平时").grid(row=1,column=4)
Label(master, text="考试").grid(row=2,column=0)
Label(master, text="总分").grid(row=3,column=0)

e1 = Entry(master,textvariable = number)
e1.grid(row=0, column=1, padx=10, pady=5)
e2 = Entry(master,textvariable = name,state='disabled').grid(row=1, column=3, padx=10, pady=5)
e3 = Entry(master,textvariable = score_1,state='disabled').grid(row=1, column=5, padx=10, pady=5)
e4 = Entry(master,textvariable = score_2,state='disabled').grid(row=2, column=1, padx=10, pady=5)
e5 = Entry(master,textvariable = score,state='disabled').grid(row=3,column=1, padx=10, pady=5)
e6 = Entry(master,textvariable = number_show,state='disabled').grid(row=1,column=1, padx=10, pady=5)
#加入show="*"
def show():
    index = e1.get().strip()
    index = student_hash.get(index,-1)
    if index == -1:
        number_show.set("未找到学号")
        name.set()
        score_1.set("")
        score_2.set("")
        score.set("")
    else:
        data = students[index]
        number_show.set(data.number)
        name.set(data.name)
        score_1.set(data.score_1)
        score_2.set(data.score_2)
        score.set(data.score)
        
Button(master, text="获取信息", width=10, command=show).grid(row=0, column=2, padx=10, pady=5)
#stick表示方位

mainloop()
