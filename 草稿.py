def x(s,p):
    s_iter=iter(s)
    method_1=0      #检测到.启动方法一
    method_2=0      #检测到*启动方法二
    for p_i in range(len(p)):
        if p(p_i)=='.':
            method_1=1
        try:
            if p(p_i+1)=='*':
                method_2=1
        except IndexError:
            pass
        if method_1==1 and method_2==1:
            if p(p_i+2)==