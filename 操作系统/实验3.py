class Freelink:
    def __init__(self, lens, fix):
        self.ram = [0 for _ in range(lens)]
        self.ram[:fix] = [1]*fix
        self.id = {"系统":[0,64]}
        self.sort()

    def sort(self):
        i, j = 0, 0
        self.pos = []
        while j < len(self.ram):
            i = j + self.ram[j:].index(0)
            try:
                j = i + self.ram[i:].index(1)
            except ValueError:
                j = len(self.ram)
            self.pos.append([i,j,j-i])
        self.pos.sort(key = lambda x: -x[2])

    def distribution(self, lens, id):
        if lens > self.pos[0][2]:
            return False
        i = self.pos[0][0]
        self.ram[i:i+lens] = [1]*lens
        self.id[id] = [i,i+lens]
        self.sort()
        return True

    def free(self, id):
        i, j = self.id.pop(id)
        self.ram[i:j] = [0]*(j-i)
        self.sort()

    def show(self):
        print("当前的空闲分区链为")
        for i in range(len(self.pos)):
            print("第%s块区域---起始点:%s, 大小为:%s"%(i+1, self.pos[i][0], self.pos[i][2]))
        print()
        for id in self.id:
            print("%s在%s-%s区域"%(id,self.id[id][0],self.id[id][1]))

a = Freelink(640,64)
print("----------------------------------------------------------------\nt1时刻：")
a.show()
a.distribution(8,'a')
a.distribution(16,'b')
a.distribution(64,'c')
a.distribution(124,'d')
print("----------------------------------------------------------------\nt2时刻：")
a.show()
a.free('c')
print("----------------------------------------------------------------\nt3时刻：")
a.show()
a.distribution(50,'e')
print("----------------------------------------------------------------\nt4时刻：")
a.show()
a.free('d')