def combine(n: int, k: int):
    if n <= 0 or k <= 0 or k > n:
        return []
    temp=[ i for i in range(1,n+1)]
    res=[]

    def count(base_temp,list_temp,k):
        #递归循环内部排列
        nonlocal res
        if k==1:
            #在最深层将临时基表分别添加后面元素并传进结果列表
            for each in list_temp:
                base_temp.append(each)
                res.append(base_temp[:])
                base_temp.pop()
            return
        for each in list_temp:
            if len(list_temp[list_temp.index(each)+1:])<k-1:
                #结束条件:后面剩余的数据已经不足以支持完成k个数
                return
            base_temp.append(each)
            count(base_temp[:],list_temp[list_temp.index(each)+1:],k-1)
            base_temp.pop()
    count([],temp,k)
    return res

combine(5,3)
