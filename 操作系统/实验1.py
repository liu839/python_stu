class Pcb:
    def __init__(self, pid, status, priority, name, cputime):
        self.pid = pid
        self.status = status
        self.priority = priority
        self.cputime = cputime
        self.name = name
pcbs = []
pcbs_wait = []
def create():
    pid = int(input("请输入pid:"))
    status = int(input("请输入初始状态:"))
    priority = input('请输入进程优先级:')
    name = input("请输入进程名称:")
    cputime = int(input('请输入需要运行的时间片个数:'))
    if status:
        pcbs.append(Pcb(pid, status, priority, name, cputime))
    else:
        pcbs_wait.append(Pcb(pid, status, priority, name, cputime))

def run():
    if pcbs:
        print("\n运行进程有")
        for each in pcbs:
            print("name:%s, pid:%s, priority:%s, cputime:%s, status:%s"%(each.name, each.pid, each.priority, each.cputime, each.status))
    else:
        print("没有正在进行的进程\n")
    if pcbs_wait:
        print("\n就绪进程有")
        for each in pcbs_wait:
            print("name:%s, pid:%s, priority:%s, cputime:%s, status:%s"%(each.name, each.pid, each.priority, each.cputime, each.status))
    else:
        print("没有阻塞的进程\n")

def huanchu(): 
    while True:
        name_out = input("请输入需要换出的名称")
        if name_out in [each.name for each in pcbs]:
            break
        input("找不到进程,请重新输入")

    for i in range(len(pcbs)):
        if pcbs[i].name == name_out:
            pcb_out = pcbs[i]
            pcb_out.status = 0
            pcbs.remove(pcbs[i])
            print("已获取换出进程\n")
            break

    while True:
        name_in = input("请输入需要换入的名称")
        if name_in in [each.name for each in pcbs_wait]:
            break
        input("找不到进程,请重新输入")
    
    for i in range(len(pcbs_wait)):
        if pcbs_wait[i].name == name_in:
            pcb_in = pcbs_wait[i]
            pcb_in.status = 1
            pcbs_wait.remove(pcbs_wait[i])
            print("已获取换入进程\n")
    pcbs_wait.append(pcb_out)
    pcbs.append(pcb_in)

def kill():
    while True:
        name = input("请输入需要删除的进程名称")
        if name in [each.name for each in pcbs] or name in [each.name for each in pcbs_wait]:
            break
        input("找不到进程,请重新输入")

    for i in range(len(pcbs)):
        if pcbs[i].name == name:
            pcbs.remove(pcbs[i])
            print("已删除")
            break

def get():
    print('''	********************************************
        *               进程演示系统               *
        ********************************************
            1.创建新的进程      2.查看运行进程     
            3.换出某个进程      4.杀死运行进程     
            5.退出系统         
        ********************************************''')
    while True:
        number = input("请输入(1~5):")
        try:
            number = int(number)
            if 1<= number <=5:
                return number
            print("数字不符合规范,请重新输入\n")
        except:
            print ("输入错误,请重新输入\n")
            continue

while True:
    num = get()
    if num == 1:
        create()
    elif num == 2:
        run()
    elif num == 3:
        huanchu()
    elif num == 4:
        kill()
    else:
        break


