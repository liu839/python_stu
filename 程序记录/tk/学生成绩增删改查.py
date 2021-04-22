from tkinter import Tk,StringVar,Label,Entry,Button,mainloop
from  tkinter  import ttk
from easygui import msgbox,fileopenbox
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
				self.score_1 = int(score_1) if score_1 else 0
				self.score_2 = int(score_2) if score_2 else 0
				self.score = self.score_1*0.4 + self.score_2*0.6
		def __set__(self,instance,value):
				print(instance,value)
students = []

flag = True
while flag:
	file_name = fileopenbox(msg="请选择目标文件")
	if file_name[-11:] == "student.txt":
		flag = False
	else:
		msgbox(msg="选择文件名不为student.txt无法打开")

with open(file_name, 'r') as f:
		data = list(f)
		for index,each in enumerate(data):
				each = each.replace('\n', '')
				each = each.split(' ')
				students.append(Student(each[0],each[1],int(each[2]),int(each[3])))

				student_hash[each[0]] = students[-1]

def show(*args):
		data = e1.get().strip()
		data = student_hash.get(data,-1)
		if data == -1:
				number_show.set("未找到学号")
				name.set("")
				score_1.set("")
				score_2.set("")
				score.set("")
		else:
				number_show.set(data.number)
				name.set(data.name)
				score_1.set(data.score_1)
				score_2.set(data.score_2)
				score.set(data.score)
				
# def add():
#   data = Student(number_show.get(), name.get(), score_1.get(), score_2.get())
#   students.append(data)
#   student_hash[data.number] = len(students)-1
#   e1['values'] += (data.number,)
# def change():
# 	pass
# def chooseMenu():
#   b2.grid_remove()
#   b3.grid_remove()
#   b1.grid()
# def addMenu():
#   b1.grid_remove()
#   b3.grid_remove()
#   b2.grid()
# def changeMenu():
#   b2.grid_remove()
#   b1.grid()
#   b3.grid()
# menubar = Menu(master)
# choosemenu = Menu(menubar, tearoff=0)

# menubar.add_cascade(label='选择功能', menu=choosemenu)
# choosemenu.add_command(label='查找', command=chooseMenu)
# choosemenu.add_command(label='添加', command=addMenu)
# choosemenu.add_command(label='修改', command=changeMenu)

# master.config(menu=menubar)

Label(master, text="输入学号").grid(row=0)

Label(master, text="学号").grid(row=1,column=0)
Label(master, text="姓名").grid(row=1,column=2)
Label(master, text="平时").grid(row=2,column=0)
Label(master, text="考试").grid(row=2,column=2)
Label(master, text="总分").grid(row=3,column=0)

e1 = ttk.Combobox(master,textvariable = number) #初始化
e1['values'] = [each.number for each in students] 
# e1.current(0)
e1.bind("<<ComboboxSelected>>")

e1.grid(row=0, column=1, padx=10, pady=5)

e2 = Entry(master,textvariable = name).grid(row=1, column=3, padx=10, pady=5)
e3 = Entry(master,textvariable = score_1).grid(row=2, column=1, padx=10, pady=5)
e4 = Entry(master,textvariable = score_2).grid(row=2, column=3, padx=10, pady=5)
e5 = Entry(master,textvariable = score).grid(row=3,column=1, padx=10, pady=5)
e6 = Entry(master,textvariable = number_show).grid(row=1,column=1, padx=10, pady=5)
#加入show="*"

b1 = Button(master, text="查找信息", width=10, command=show)
b1.grid(row=0, column=2, padx=10, pady=5)
#stick表示方位
# b2 = Button(master, text="添加信息", width=10, command=add)
# b2.grid(row=0, column=2, padx=10, pady=5)
# b2.grid_remove()

# b3 = Button(master, text="修改信息", width=10, command=change)
# b3.grid(row=0, column=3, padx=10, pady=5)
# b3.grid_remove()
mainloop()
