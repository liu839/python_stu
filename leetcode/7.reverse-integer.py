def reverse(x):
    if x<-pow(2,31) or x>pow(2,31)-1:
        return 0
    str1=''
    str_x=str(x)
    len_x=len(str_x)
    dict_temp=dict()
    if '-' in str_x:
        str_x=str_x[1:]
        for i in range(len_x):
            dict_temp[i]=str(x)[i]
        str1+='-'
        for i in range(len_x-1):
            str1+=dict_temp[len_x-1-i]
    else:
        for i in range(len_x):
            dict_temp[i]=str(x)[i]
        for i in range(len_x):
            str1+=dict_temp[len_x-1-i]
    if int(str1)<-pow(2,31) or int(str1)>pow(2,31)-1:
        return 0
    return int(str1)

""" def reverse(self, x: int) -> int:
        y=int(str(x)[::-1]) if x>=0 else -int(str(x)[:0:-1])
        return y if -2**31<y<2**31-1 else 0 
        
    7.15添加做法    
"""
print(reverse(-12300))
