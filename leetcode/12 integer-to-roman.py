def solv(num):
    dict_={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    str_=''
    key=iter(dict_)
    each=key.__next__()
    while True:
        if num == 0:
            break
        if num - each < 0:
            each = key.__next__()
        else:
            num -= each
            str_ += dict_[each]
    return str_

def solv2(num):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    str_ = ''

    key=iter(nums)
    each=key.__next__()
    while True:
        if num == 0:
            break
        if num < each:
            each = key.__next__()
        else:
            num-=each
            str_+=romans[nums.index(each)]
    return str_
print(solv2(3))
