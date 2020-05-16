def a(s):
    dict_={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'V':5,'IX':4,'I':1,'M':1000,'D':500,'C':100,'L':50,'X':10}
    sum_=0
    for each in dict_:
        if not len(s):
            break
        while each in s:
            s=s.replace(each,"",1)
            sum_+=dict_[each]
    return sum_
print(a("III"))