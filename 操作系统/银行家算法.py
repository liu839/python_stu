class Mylist(list):
    def __init__(self,list_):
        super().__init__(list_)
    def __add__(self, other):
        return Mylist([a+b for a,b in zip(self, other)])
    def __sub__(self, other):
        return Mylist([a-b for a,b in zip(self, other)])
    def __ge__(self, other):
        for each in self-other:
            if each < 0: return False
        return True
    def __le__(self, other):
        for each in self-other:
            if each > 0: return False
        return True
    def __iadd__(self, other):
        return self + other
    def __isub__(self, other):
        return self - other

class Process():
    def __init__(self, Max, Allocation, Need, id):
        self.id = id
        self.max_ =  Mylist(Max)
        self.allocation = Mylist(Allocation)
        self.need = Mylist(Need)
        
available = Mylist([3, 3 ,2])
p = [
    Process([7, 5, 3], [0, 1, 0], [7, 4, 3], 0),
    Process([3, 2, 2], [2, 0, 0], [1, 2, 2], 1),
    Process([9, 0, 2], [3, 0, 2], [6, 0, 0], 2),
    Process([2, 2, 2], [2, 1, 1], [0, 1, 1], 3),
    Process([4, 3, 3], [0, 0, 2], [4, 3, 1], 4)
    ]

def test(p, work, id_list, used):
    if not p:
        print("已找到安全序列", id_list)
        raise EOFError
    p_queue = [a for a in p if a.need <= work]

    while p_queue:
        p_temp = p_queue.pop(0)
        used.append(p_temp)
        test([y for y in p if y not in used], work+p_temp.allocation, id_list + [p_temp.id], used)
        used.pop()

def banker(p, available ,request, id):
    p.sort(key=lambda x:x.id!=id)
    process_re = p.pop(0)
    if not process_re.need >= request:
        print("需求大于申请,驳回")
        return
    if not available >= request:
        print("资源不足,请求失败")
        return

    process_re.allocation += request
    process_re.need -= request
    available -= request

    p.insert(0,process_re)
    try:
        test(p, available, [], [])
        print("会出现不安全状态")
        return
    except EOFError:
        return

banker(p, available, Mylist([1, 0, 2]), 1)