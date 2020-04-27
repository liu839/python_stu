def input_int():
    while True:
        try:
            temp=input("请输入")
            break
        except ValueError:
            print("输入错误重新输入")
    return temp
            #KeyboardInterrupt(文件末尾endoffile，当用户按下组合键 Ctrl+d 产生) 
            #EOFError(取消输入，当用户按下组合键 Ctrl+c 产生)
            #这里还有两种异常可以被捕获
#整个函数运行会收集一个整型数据返回