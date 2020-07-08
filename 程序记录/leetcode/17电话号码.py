def x(digits):
    dict_={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    res=[]
    def solv(s,temp): 
        nonlocal dict_,res
        if s=='':
            res.append([temp[:]])
            return
        str_=dict_[s[0]]
        for each in str_:
            solv(s[1:],(temp+each)[:])
    solv(str(digits),'')
    return res
print(x("23"))