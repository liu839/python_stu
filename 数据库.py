from faker import Factory
import random
class User():
    def __init__(self, name, password, email, address):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
class Shop():
    def __init__(self, name, obj_name, number, status):
        self.name = name
        self.obj_name = obj_name
        self.number = number
        self.status = status
class Order():
    def __init__(self, id, name, address, cost, status):
        self.id = id
        self.name = name
        self.address = address
        self.cost = cost
        self.status = status
class Order_chl():
    def __init__(self, id, name, obj_name):
        self.id = id
        self.name = name
        self.obj_name = obj_name
class Pay():
    def __init__(self, id, name, environ, status):
        self.id = id
        self.name = name
        self.environ = environ
        self.status = status
class Obj():
    def __init__(self, sort, obj_name, obj_pri):
        self.sort = sort
        self.obj_name = obj_name
        self.obj_pri = obj_pri


temp_shop = ['已勾选', '未勾选']
temp_order = ['已付款', '未付款']
temp_pay_en = ['淘宝','京东','拼多多','唯品会']
temp_pay = ['支付成功','支付失败']
temp_obj = ['衣','食','住','行']
fake = Factory().create('zh_CN')
users ,shops, orders, orders_chl, pays, objs= [], [], [], [], [], []
obj_name_ = []
for _ in range(30):
    name = fake.name()
    while True:
        obj_name = fake.color_name()
        if obj_name not in obj_name_:
            obj_name_.append(obj_name)
            break
    users.append(User(name, fake.password(), fake.email(), fake.address()))
    objs.append(Obj(temp_obj[random.randint(0,3)],obj_name,random.randint(1,1000)))
    shops.append(Shop(name=name, obj_name='None' , number= random.randint(1,500),status=temp_shop[random.randint(0,1)]))
#print("INSERT INTO `用户` (`用户名`, `密码`, `邮箱`) VALUES ",end="")

for index in range(30):
    i = random.randint(0,29)
    id = fake.ean8()
    shops[index].obj_name = objs[i].obj_name
    orders.append(Order(id, users[i].name, users[i].address, random.randint(1,1000), temp_order[random.randint(0,1)]))
    orders_chl.append(Order_chl(id, users[i].name,fake.color_name()))
    pays.append(Pay(id, users[random.randint(0,29)].name, temp_pay_en[random.randint(0,3)], temp_pay[random.randint(0,1)]))

print("INSERT INTO `商品表` (`分类`, `商品名称`, `商品单价`) VALUES('a','A','1') ",end = "")
for each in objs:
    print(",\n('%s','%s','%s')"%(each.sort, each.obj_name, each.obj_pri),end = "")
print(';\n')
print("INSERT INTO `支付` (`订单号`, `用户名`, `支付平台`, `支付状态`) VALUES ('1', 'A', 'a', 'a')",end = "")
for each in pays:
    print(",\n('%s','%s','%s','%s')"%(each.id, each.name, each.environ, each.status),end = "")
print(';\n')
print("INSERT INTO `用户` (`用户名`, `密码`, `邮箱`, `收获地址`) VALUES ('A', 'A', 'A@qq.com', 'asd1')",end="")
for each in users:
    print(",\n('%s','%s','%s','%s')"%(each.name, each.password, each.email, each.address),end = "")
print(';\n')
print("INSERT INTO `订单` (`订单号`, `用户名`, `收获地址`, `付款金额`, `订单状态`) VALUES ('11', 'A', 'asd1', '1', '1')",end="")
for each in orders: 
    print(",\n('%s','%s','%s', '%s','%s')"%(each.id, each.name, each.address, each.cost, each.status),end = "")
print(';\n')
print("INSERT INTO `订单子表` (`订单号`, `用户名`, `商品名`) VALUES ('11', 'sad', 'as')",end = "")
for each in orders_chl:
    print(",\n('%s','%s','%s')"%(each.id, each.name, each.obj_name),end = "")
print(';\n')
print("INSERT INTO `购物车` (`用户名`, `商品名`, `数量`, `勾选状态`) VALUES ('A', 'as', '1', '1')",end = "")
for each in shops:
    print(",\n('%s','%s','%s','%s')"%(each.name, each.obj_name, each.number, each.status),end = "")
print(';\n')
