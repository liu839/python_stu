n = int(input())
dict_term = {}
def touch(data,time):
    global dict_term
    if data not in dict_term:
        dict_term[data] = time

def rename(bef,aft):
    global dict_term
    if aft in dict_term or bef not in dict_term:
        return
    dict_term[aft] = dict_term.pop(bef)

def delete(data):
    global dict_term
    if data not in dict_term:
        return
    dict_term.pop(data)

def output():
    global dict_term
    a = [each for each in dict_term]
    a.sort(key=lambda x:dict_term[x])
    for each in a:
        print(each)

data_ = []
for i in range(n):
    data = input().split(" ")
    if data[0] == "touch":
        touch(data[1],i)
        continue
    if data[0] == "rename":
        rename(data[1],data[2])
        continue
    if data[0] == "rm":
        delete(data[1])
        continue
    if data[0] == "ls":
        output()