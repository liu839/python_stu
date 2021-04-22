x = [0.2, 0.4, 0.6, 0.8, 1.0]
y = [0.98, 0.92, 0.81, 0.64, 0.38]

def counts(x,y,res):
    if len(y)==1:
        return res
    y_new = []
    for i in range(len(y)-1):
        y_new.append(round((y[i+1]-y[i])/(x[i+1+len(res)]-x[0]),4))
    res.append(y_new)
    return counts(x,y_new,res)

res = counts(x,y,[])
p = str(y[0])

for each in range(len(res)):
    if res[each][0]<0:
        flag = ""
    else:
        flag ="+"

    p =p + flag + str(res[each][0])
    for i in range(each+1):
        p = p+"(x-"+str(x[i])+")"

print(p)
