def a(s):
    dict_change={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4,'I':1,'V':5,'M':1000,'D':500,'C':100,'L':50,'X':10}
    sum_=0
    for each in dict_change:
        if not len(s):
            break
        while each in s:
            s=s.replace(each,"",1)
            sum_+=dict_change[each]
    return sum_

def b(s):
    dict_change={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res=0
    try:
        for index,each in enumerate(s):
            if dict_change[each] < dict_change[s[index + 1]]:
                res -= dict_change[each]
            else:
                res += dict_change[each]
    except IndexError:
        res += dict_change[s[-1]]
    return res


print(b("LVIII"))