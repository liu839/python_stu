
import os

os.getcwd()
#返回当前工作目录
import numpy as np
import matplotlib.pyplot as plt
import random
def show(iter):
    global pathbest
    plt.ion()
    # 作出找到的最优路径图
    bestpath = pathbest[iter]

    plt.plot(coordinates[:, 0], coordinates[:, 1], 'r.', marker='>')
    plt.xlim([-100, 2000])
    #x范围
    plt.ylim([-100, 1500])
    #y范围

    for i in range(numcity - 1):
        #按坐标绘出最佳两两城市间路径
        m, n = int(bestpath[i]), int(bestpath[i + 1])
        print("best_path:",m, n)
        plt.plot([coordinates[m][0],coordinates[n][0]],   [coordinates[m][1], coordinates[n][1]],  'k')

    plt.plot([coordinates[int(bestpath[0])][0],coordinates[int(bestpath[-1])][0]],    [coordinates[int(bestpath[0])][1],coordinates[int(bestpath[-2])][1]]   ,'b')

    ax = plt.gca()
    ax.set_title("Best Path,No.%s"%(iter+1))
    ax.set_xlabel('X_axis')
    ax.set_ylabel('Y_axis') 
    #plt.savefig('Best Path.png', dpi=500, bbox_inches='tight')
    plt.show()
    plt.pause(0.1)
    if iter < 99:
        plt.clf()

#初始化城市坐标
def get_data(n):
    res = []
    for _ in range(n):
        while True:
            temp = [random.randint(0,2000),random.randint(0,1400)]
            if temp not in res:
                res.append(temp)
                break
    return res
#coordinates = np.array(get_data(50))
coordinates = np.array([[565.0, 575.0], [25.0, 185.0], [345.0, 750.0], [945.0, 685.0], [845.0, 655.0],
                        [880.0, 660.0], [25.0, 230.0], [525.0, 1000.0], [580.0, 1175.0], [650.0, 1130.0],
                        [1605.0, 620.0], [1220.0, 580.0], [1465.0, 200.0], [1530.0, 5.0], [845.0, 680.0],
                        [725.0, 370.0], [145.0, 665.0], [415.0, 635.0], [510.0, 875.0], [560.0, 365.0],
                        [300.0, 465.0], [520.0, 585.0], [480.0, 415.0], [835.0, 625.0], [975.0, 580.0],
                        [1215.0, 245.0], [1320.0, 315.0], [1250.0, 400.0], [660.0, 180.0], [410.0, 250.0],
                        [420.0, 555.0], [575.0, 665.0], [1150.0, 1160.0], [700.0, 580.0], [685.0, 595.0],
                        [685.0, 610.0], [770.0, 610.0], [795.0, 645.0], [720.0, 635.0], [760.0, 650.0],
                        [475.0, 960.0], [95.0, 260.0], [875.0, 920.0], [700.0, 500.0], [555.0, 815.0],
                        [830.0, 485.0], [1170.0, 65.0], [830.0, 610.0], [605.0, 625.0], [595.0, 360.0],
                        [1340.0, 725.0], [1740.0, 245.0]])

#计算城市间的欧式距离
def getdistmat(coordinates):
    num = coordinates.shape[0]
    distmat = np.zeros((len(coordinates), len(coordinates)))
    # 初始化生成52*52的矩阵
    for i in range(num):
        for j in range(i, num):
            distmat[i][j] = distmat[j][i] = np.linalg.norm(coordinates[i] - coordinates[j])
    return distmat

#初始化数据
distmat = getdistmat(coordinates)
numant = 60  # 蚂蚁个数
numcity = coordinates.shape[0]
# shape[0]=52 城市个数,也就是任务个数
alpha = 1  # 信息素重要程度因子
beta = 5   # 启发函数重要程度因子
rho = 0.5  # 信息素的挥发速度
Q = 1      # 完成率

iter = 0       #迭代初始
itermax = 100   #迭代总数

etatable = 1.0 / (distmat + np.diag([1e10] * numcity))
#diag(),将一维数组转化为方阵 启发函数矩阵，表示蚂蚁从城市i转移到城市j的期望程度
pheromonetable = np.ones((numcity, numcity))
# 信息素矩阵
pathtable = np.zeros((numant, numcity)).astype(int)
# 路径记录表

lengthaver = np.zeros(itermax)  # 存放每次迭代后，路径的平均长度  
lengthbest = np.zeros(itermax)  # 存放每次迭代后，最佳路径长度  
pathbest = np.zeros((itermax, numcity))  # 存放每次迭代后，最佳路径城市的坐标 

while iter < itermax:
    #迭代总数

    #蚂蚁随机放置于城市中
    if numant <= numcity:  # 城市数比蚂蚁数多，不用管
        pathtable[:, 0] = np.random.permutation(range(numcity))[:numant]
        #矩阵的意思是哪个蚂蚁在哪个城市,矩阵元素不大于52,是一个打乱的矩阵
    else:  # 蚂蚁数比城市数多，需要有城市放多个蚂蚁
        pathtable[:numcity, 0] = np.random.permutation(range(numcity))[:]
        pathtable[numcity:, 0] = np.random.permutation(range(numcity))[:numant - numcity]
    length = np.zeros(numant)

    #本段程序算出每只/第i只蚂蚁转移到下一个城市的概率
    for i in range(numant):

        visiting = pathtable[i, 0]  # 当前所在的城市
        unvisited = set(range(numcity))
        #未访问的城市集合
        unvisited.remove(visiting)  # 删除已经访问过的城市元素

        for j in range(1, numcity):  #访问剩余的所有numcity-1个城市
            # 每次用轮盘法选择下一个要访问的城市
            listunvisited = list(unvisited)
            #未访问城市数,list
            probtrans = np.zeros(len(listunvisited))
            #每次循环都初始化转移概率矩阵


            #以下是计算转移概率
            for k in range(len(listunvisited)):
                probtrans[k] = np.power(pheromonetable[visiting][listunvisited[k]], alpha) \
                               * np.power(etatable[visiting][listunvisited[k]], alpha)
            #eta-从城市i到城市j的启发因子 这是概率公式的分母   其中[visiting][listunvis[k]]是从本城市到k城市的信息素
            cumsumprobtrans = (probtrans / sum(probtrans)).cumsum()

            cumsumprobtrans -= np.random.rand()
            # 随机生成下个城市的转移概率，再用区间比较

            k = listunvisited[list(cumsumprobtrans > 0).index(True)]
            # 下一个要访问的城市

            pathtable[i, j] = k
            #采用禁忌表来记录蚂蚁i当前走过的第j城市的坐标，这里走了第j个城市.k是中间值
            unvisited.remove(k)
            # visited.add(k)
            #将未访问城市列表中的K城市删去，增加到已访问城市列表中

            length[i] += distmat[visiting][k]
            #计算本城市到K城市的距离
            visiting = k

        length[i] += distmat[visiting][pathtable[i, 0]]
        # 计算本只蚂蚁的总的路径距离，包括最后一个城市和第一个城市的距离

    # print("ants all length:",length)
    # 包含所有蚂蚁的一个迭代结束后，统计本次迭代的若干统计参数

    lengthaver[iter] = length.mean()
    #本轮的平均路径



    #求最佳路径
    if iter == 0:
        lengthbest[iter] = length.min()
        pathbest[iter] = pathtable[length.argmin()].copy()
    #如果是第一轮路径，则选择本轮最短的路径,并返回索引值下标，并将其记录
    else:
    #后面几轮的情况，更新最佳路径
        if length.min() > lengthbest[iter - 1]:
            lengthbest[iter] = lengthbest[iter - 1]
            pathbest[iter] = pathbest[iter - 1].copy()
        # 如果是第一轮路径，则选择本轮最短的路径,并返回索引值下标，并将其记录
        else:
            lengthbest[iter] = length.min()
            pathbest[iter] = pathtable[length.argmin()].copy()


    #此部分是为了更新信息素
    changepheromonetable = np.zeros((numcity, numcity))
    for i in range(numant):#更新所有的蚂蚁
        for j in range(numcity - 1):
            changepheromonetable[pathtable[i, j]][pathtable[i, j + 1]] += Q / distmat[pathtable[i, j]][pathtable[i, j + 1]]
            #根据公式更新本只蚂蚁改变的城市间的信息素      Q/d   其中d是从第j个城市到第j+1个城市的距离
        changepheromonetable[pathtable[i, j + 1]][pathtable[i, 0]] += Q / distmat[pathtable[i, j + 1]][pathtable[i, 0]]
        #首城市到最后一个城市 所有蚂蚁改变的信息素总和

    #信息素更新公式p=(1-挥发速率)*现有信息素+改变的信息素
    pheromonetable = (1 - rho) * pheromonetable + changepheromonetable

    iter += 1  # 迭代次数指示器+1
    print("this iteration end：",iter)
    if (iter - 1) % 20 == 0:
        print("schedule:",iter - 1)
    show(iter-1)
#迭代完成



#以下是做图部分
#做出平均路径长度和最优路径长度
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
axes[0].plot(lengthaver, 'k', marker='*')
axes[0].set_title('Average Length')
axes[0].set_xlabel(u'iteration')

axes[1].plot(lengthbest, 'k', marker='<')
axes[1].set_title('Best Length')
axes[1].set_xlabel(u'iteration')
#fig.savefig('Average_Best.png', dpi=500, bbox_inches='tight')
plt.ioff()
plt.show()
plt.close()

