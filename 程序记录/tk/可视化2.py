import json
provice = {}
city ={}
city_list = []
with open(r".\程序记录\tk\省市.txt","rb") as f:
    data = json.load(f)
for pro in data:
    data = pro["city"]
    pro_name = pro["name"]
    city_list = []
    for ci in data:
        city_list.append(ci["name"])
        city[ci["name"]] = ci["area"]
    provice[pro_name] = city_list
print(list(provice.keys()))