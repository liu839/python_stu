def x(strs):
    #        return os.path.commonprefix(strs)  #less is more
    l=len(strs)
    if l==0 or ("" in strs):
        return ""
    elif l==1:
        return strs[0]
    str_=''
    i=j=0
    while True:
        for index in range(l-1):
            try:
                if strs[index][i]!=strs[index+1][i]:
                    break
                j+=1
            except IndexError:
                return str_
        if j==l-1:
                str_+=strs[index][i]
            i+=1
            j=0
        else:
            return str_
print(x(["flower","flow","flight"]))

