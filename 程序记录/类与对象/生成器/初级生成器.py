def myrev(string):
    temp=list(string)
    while True:
        try:
            yield temp.pop()
        except IndexError:
            break
for i in myrev("fishc"):
    print(i,end='')