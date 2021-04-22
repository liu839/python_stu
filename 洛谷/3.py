class Stu():
    def __init__(self,t,k,i):
        self.t = t
        self.k = k
        self.i = i
t = int(input())
stu = []
for i in range(t):
    data = [int(each) for each in input().split(' ')]
    stu.append(Stu(data[0],data[1],i+1))
stu.sort(key=lambda x:(-x.k*x.t,-x.t,x.i))
a = ' '.join([str(each.i) for each in stu])
print(a)
