import random
class Pcb():
    def __init__(self, pid, state, cpu_time) -> None:
        self.pid = pid
        self.state = state
        self.cpu_time = cpu_time

blocked = []
ready = []

n, m, t = 2, 3, 5
def start(n,m):
    global blocked, ready
    for i in range(n):
        ready.append(Pcb(i,1,random.randint(1,5)))
    for i in range(m):
        blocked.append(Pcb(i+n,0,random.randint(1,5)))
    print("初始化完成，数据为")
    for each in ready+blocked:
        print("pid:%s, state:%s, cpu_time:%s"%(each.pid, each.state, each.cpu_time))
    print("\n")
start(n, m)
time_use = 0
time_unuse = 0
while ready or blocked:
    if ready:
        p = ready.pop(0)
        p.cpu_time -=1
        time_use += 1
        if not p.cpu_time:
            print("时间：%s已完成%s"%(time_use, p.pid))
        else:
            ready.append(p)
        if not((time_use+time_unuse) % 4) and blocked:
            ready.append(blocked.pop(0))
    else:
        time_unuse += 1
        if not((time_use+time_unuse) % 4) and blocked:
            ready.append(blocked.pop(0))
print("\n已全部完成\ntime_use:%s, time_unuse:%s\n效率为%.2f%%, "%(time_use, time_unuse, time_use*100/(time_use+time_unuse)))