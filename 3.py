data = input().split("=")
a = float(''.join([a for a in data[0] if a.isdigit()]))
b = data[0].replace(str(int(a)), "")
res_ = data[1].replace("?", "")
dict_={
"GBMB":2**10, "GBKB":2**20, "GBB":2**30, "GBGB":1,
"MBGB": 1/(2**10), "MBKB":2**10, "MBB":2**20, "MBMB":1,
"KBGB": 1/(2**20),"KBMB":1/(2**10), "KBB":2**10, "KBKB":1,
"BGB": 1/(2**30),"BMB":1/(2**20), "BKB":1/(2**10), "BB":1,}
print("%.6f"%(a * dict_[b+res_]))